import hashlib
import dateparser
import re


def layso(XAU,DAU):
    if not XAU is None:
        xau=re.sub(r"([^0-9"+DAU+"])","", str(XAU).strip())
        if 'K' in str(XAU):
            xau=str(round(float(xau)*1000,2))
        if 'M' in str(XAU):
            xau=str(round(float(xau)*1000000,2))
        if 'B' in str(XAU):
            xau=str(round(float(xau)*1000000000,2))    
    else:
        xau=''
    return xau

def key_MD5(xau):
    xau=(xau.upper()).strip()
    KQ=hashlib.md5(xau.encode('utf-8')).hexdigest()
    return KQ
def comparestr(xau1,xau2):
    xau1=str(str(xau1).lower()).replace(',','')
    xau2=str((str(xau2).lower()).split()).replace(',','')
    KQ=0
    X1=str(xau1).split()
    for rs in X1:
        if rs in xau2:
            KQ+=1
    return KQ
def CHECK_QUE_ALL(conn):
    KQ=KQ1=KQ2=0
    cur = conn.cursor()
    cur.execute("SELECT COUNT(1) FROM deftrandest WHERE dblink='WVBHN.US.WVB.COM'")       
    rcs = cur.fetchone()    
    if rcs:
        KQ1=rcs[0]
    cur.close()
    cur = conn.cursor()
    cur.execute("SELECT COUNT(1) FROM deftrandest WHERE dblink='WVBKL.US.WVB.COM'")       
    rcs = cur.fetchone()    
    if rcs:
        KQ2=rcs[0]
    cur.close()
    KQ=max(KQ1,KQ2)
    return KQ
def CHECK_QUE(conn):
    KQ=0
    cur = conn.cursor()
    cur.execute("SELECT COUNT(1) FROM deftrandest WHERE dblink='WVBHN.US.WVB.COM'")       
    rcs = cur.fetchone()
    if rcs:
        KQ=rcs[0]
    cur.close()
    return KQ
def Get_ID(FIELD,conn):
    # FIELD = PRICE_ID_SEQ , CROSS_REF_SEQ , INDEX_PERM_ID
    ID=0
    cur = conn.cursor()
    cur.execute("SELECT "+FIELD+".NEXTVAL as id FROM DUAL")       
    rcs = cur.fetchone()
    if rcs:
        ID=rcs[0]
    cur.close()
    return ID
def get_more_data(ISIN,conn):
    item={}
    cur = conn.cursor()
    sql="SELECT WVB_COMPANY.COMPANY_PERM_ID,EQUITY_SECURITY.EQUITY_SEC_PERM_ID,WVB_COMPANY.WVB_NUMBER,WVB_COMPANY.PRIMARY_SHORT_COMPANY_NAME,WVB_COMPANY.PRIMARY_LONG_COMPANY_NAME,EQUITY_SECURITY.ISIN_FROM_REPORT,WVB_COMPANY.WVB_STAT_CODE_INTERNAL,EQUITY_SECURITY.SEC_CLASSIF_CODE,decode(WVB_COMPANY.WVB_STAT_CODE_INTERNAL, '90', 1, '11', 2, '15', 3, '91', 4, 100) code_order,decode( EQUITY_SECURITY.SEC_CLASSIF_CODE, 'ORD', 1, 100) type_order FROM EQUITY_SECURITY INNER JOIN WVB_COMPANY ON WVB_COMPANY.COMPANY_PERM_ID = EQUITY_SECURITY.COMPANY_PERM_ID WHERE TRIM (UPPER (ISIN_FROM_REPORT)) = '"+str(ISIN)+"' ORDER BY code_order, type_order,  EQUITY_SECURITY.SEC_CLASSIF_CODE desc"
    cur.execute(sql)
    row = cur.fetchone()
    if row:
        item['COMPANY_PERM_ID']=str(row[0])
        item['EQUITY_SEC_PERM_ID']=str(row[1])
    cur.close()
    #print('More data:',item)
    return item
def Get_INDEX_PERM_ID_IN_WVB_INDEX_CODES(MIC,FIELD,VALUE,conn):
    INDEX_PERM_ID=0
    cur = conn.cursor()
    sql="SELECT INDEX_PERM_ID FROM WVB_INDEX_CODES WHERE UPPER(INDEX_MIC)='" + MIC.upper()+ "' AND UPPER("+FIELD+")='"+VALUE.upper()+"'"
    #print(sql)
    cur.execute(sql)       
    rcs = cur.fetchone()
    if rcs:
        INDEX_PERM_ID=rcs[0]
    cur.close()
    return INDEX_PERM_ID
def get_data_from_sql(conn,SQL):
    #print(SQL)
    cur = conn.cursor()
    cur.execute(SQL)
    columns = [col[0] for col in cur.description]
    DATA=[dict(zip(columns, row)) for row in cur.fetchall()]
    cur.close()
    return DATA
def RUNSQL(sql,connstr):
    RUN=0
    #print(sql)
    try:
        curinsert = connstr.cursor()
        curinsert.execute(sql)
        connstr.commit()
        RUN=1
        curinsert.close()
    except:
        pass
    return RUN
def Update_cross_ref(HEADER,item,ITEM,conn):
    UPDATE=''
    for i in range(len(HEADER)):
        key=HEADER[i]
        if key in item:
            if key!='CROSS_REF_ID' and key!='MIC' and key!='TICKER' and key!='WHO_ENTERED' and key!='WHERE_ENTERED' and key!='DTIME_ENTERED' and str(item[key])!='' and str(item[key])!='None' and item[key]!=None:
                if key=='ISIN':
                    if len(str(item['ISIN']))>=12:
                        if UPDATE=='':
                            if(('TIME' in key) or ('DATE' in key)):
                                UPDATE=" SET "+key+"=TO_DATE('"+str(item[key])+"','yyyy-mm-dd HH24:MI:SS')"
                            else:
                                UPDATE=" SET "+key+"='"+str(item[key]).replace("'","''")+"'"
                        else:
                            if(('TIME' in key) or ('DATE' in key)):
                                UPDATE+=", "+key+"=TO_DATE('"+str(item[key])+"','yyyy-mm-dd HH24:MI:SS')"
                            else:
                                UPDATE+=", "+key+"='"+str(item[key]).replace("'","''")+"'"
                else:
                    if UPDATE=='':
                        if(('TIME' in key) or ('DATE' in key)):
                            UPDATE=" SET "+key+"=TO_DATE('"+str(item[key])+"','yyyy-mm-dd HH24:MI:SS')"
                        else:
                            UPDATE=" SET "+key+"='"+str(item[key]).replace("'","''")+"'"
                    else:
                        if(('TIME' in key) or ('DATE' in key)):
                            UPDATE+=", "+key+"=TO_DATE('"+str(item[key])+"','yyyy-mm-dd HH24:MI:SS')"
                        else:
                            UPDATE+=", "+key+"='"+str(item[key]).replace("'","''")+"'"
    if UPDATE!='':
        sql="UPDATE CROSS_REF"+UPDATE+" WHERE CROSS_REF_ID="+str(ITEM['CROSS_REF_ID'])
        #print(sql)
        RUNSQL(sql,conn)
        #print('Updated:',ITEM['CROSS_REF_ID'],'-',RUN)

def check_in_Cross_ref(HEADER,item,ITEM,conn):
    #print(item)
    #print(ITEM)
    if str(item['ISIN']).upper()==str(ITEM['ISIN']).upper() or str(ITEM['ISIN'])=='' or str(ITEM['ISIN'])=='None' or ITEM['ISIN']==None:
        #print('The same, update only')
        Update_cross_ref(HEADER,item,ITEM,conn)
    else:
        #print('Different ISIN, Copy to HIST and update')
        #Copy to HIST
        SQL="INSERT INTO CROSS_REF_HIST"
        FIELDS=""
        VALUES=""
        for i in range(0, len(HEADER)):
            key=HEADER[i]
            if(key=="WHO_LAST_CHANGED"):
                FIELDS+=key+","
                VALUES+="'TUNG',"
            elif(ITEM[key]):
                FIELDS+=key+","
                if(('TIME' in key) or ('DATE' in key)):
                    VALUES+="TO_DATE('"+str(ITEM[key])+"','yyyy-mm-dd HH24:MI:SS'),"
                else:
                    VALUES+="'"+str(ITEM[key]).replace("'","''")+"',"
        FIELDS+="HIST_DATE"
        VALUES+="SYSDATE"
        SQL=SQL+"("+FIELDS+") VALUES("+VALUES+")"
        #print(SQL)
        RUNSQL(SQL,conn)
        #print('Copy to Hist:',ITEM['CROSS_REF_ID'],'-',RUN)
        Update_cross_ref(HEADER,item,ITEM,conn)
    pass
#---------------------------------------
def Do_PRICE(item,conn):
    #print('\n --------------- \n')
    CROSS_REF_ID=0
    cur = conn.cursor()
    sql="SELECT * FROM CROSS_REF WHERE UPPER(MIC)='" + item['MIC']+ "' AND UPPER(TICKER)='"+item['TICKER']+"'"
    cur.execute(sql)
    rcs = cur.fetchall()
    ROW_NUMBER=len(rcs)
    LIST_CROSS_REF=[]
    LIST_FIELDS=[]
    for i in range(len(cur.description)):   
        key=cur.description[i][0]
        if key!='OPERATING_MIC':
            LIST_FIELDS.append(key)
            if key!='WHO_ENTERED' and key!='WHERE_ENTERED' and key!='DTIME_ENTERED':
                LIST_CROSS_REF.append(key)
    ITEM={}
    FOUND=False
    if ROW_NUMBER==1:
        #print("Found only 1 record, check ISIN ...")
        for i in range(len(cur.description)):
            ITEM[cur.description[i][0]]=rcs[0][i]
        #print('Do update ITEM - item')
        check_in_Cross_ref(LIST_FIELDS,item,ITEM,conn)
        CROSS_REF_ID=ITEM['CROSS_REF_ID']
    elif ROW_NUMBER>1:
        cur1 = conn.cursor()
        #print("Has many rows in cross_ref")
        #Get cross_ref inserting price
        sql="SELECT CROSS_REF.* FROM CROSS_REF INNER JOIN WVB_STOCK_PRICE ON CROSS_REF.CROSS_REF_ID = WVB_STOCK_PRICE.CROSS_REF_ID WHERE UPPER(MIC)='" + item['MIC']+ "' AND UPPER(TICKER)='"+item['TICKER']+"' ORDER BY CROSS_REF.ACTIVE_INACTIVE_FLAG, WVB_STOCK_PRICE.PRICE_DATE DESC"
        cur1.execute(sql)
        rcs1 = cur1.fetchone()
        if rcs1:
            for i in range(0, len(cur1.description)):
                ITEM[cur1.description[i][0]]=rcs1[i]
            FOUND=True
            #print("Found Cross ref and Price")
        if FOUND==False:
            #print("Get first record, check ISIN ...")
            for i in range(len(cur1.description)):
                ITEM[cur1.description[i][0]]=rcs[0][i]
            FOUND=True
        #print('Do update ITEM - item')
        check_in_Cross_ref(LIST_FIELDS,item,ITEM,conn)
        CROSS_REF_ID=ITEM['CROSS_REF_ID']
        #Delete other cross_ref
        for row in rcs:
            TMP={}
            for i in range(len(cur.description)):
                TMP[cur.description[i][0]]=row[i]
            if TMP['CROSS_REF_ID']!=ITEM['CROSS_REF_ID']:
                sql="UPDATE WVB_STOCK_PRICE SET CROSS_REF_ID="+str(ITEM['CROSS_REF_ID'])+" WHERE CROSS_REF_ID="+str(TMP['CROSS_REF_ID'])                
                RUNSQL(sql,conn) 
                #print('Price Deleting ...',TMP['CROSS_REF_ID'],'-',RUN)
                sql="DELETE CROSS_REF WHERE CROSS_REF_ID="+str(TMP['CROSS_REF_ID'])
                RUNSQL(sql,conn) 
                #print('Cross_ref Deleting ...',TMP['CROSS_REF_ID'],'-',RUN)
    else:
        #print("Not existed, Insert new")
        item['CROSS_REF_ID']=Get_ID('CROSS_REF_SEQ',conn)
        CROSS_REF_ID=item['CROSS_REF_ID']
        # Get more data
        if len(item['ISIN'])>=12:
            moredata=get_more_data(str(item['ISIN']),conn)
            if len(moredata)>0:
                item['COMPANY_PERM_ID']=moredata['COMPANY_PERM_ID']
                item['EQUITY_SEC_PERM_ID']=moredata['EQUITY_SEC_PERM_ID']         
            #if item['EQUITY_SEC_PERM_ID']=="":
            #item['ACTIVE_INACTIVE_FLAG']="N"
        sql="INSERT INTO CROSS_REF("
        listfiels=""
        listvalue=""
        for key,value in item.items():
            if value!=None and str(value)!="" and str(value)!="None" and (key in LIST_FIELDS):                
                if listvalue=='':
                    listfiels+=str(key)
                    if(('TIME' in key) or ('DATE' in key)):
                        listvalue+="TO_DATE('"+str(value)+"','yyyy-mm-dd')"
                    else:
                        listvalue+="'"+str(value).replace("'","''")+"'"
                else:
                    listfiels+=","+str(key)
                    if(('TIME' in key) or ('DATE' in key)):
                        listvalue+=", TO_DATE('"+str(value)+"','yyyy-mm-dd')"
                    else:
                        listvalue+=",'"+str(value).replace("'","''")+"'"
        sql=sql+listfiels+") VALUES("+listvalue+")"
        #print(sql)
        RUNSQL(sql,conn)        
        #print("*** Inserted to CROSS_REF",RUN)
    CROSS_REF={'CROSS_REF_ID':CROSS_REF_ID,'LIST':LIST_CROSS_REF}
    RUN=Insert_Price(item,CROSS_REF,conn)
    return RUN

def Insert_Price(item,CROSS_REF,conn):
    if str(item['CLOSE_PRICE'])!='' and str(item['CLOSE_PRICE'])!='None' and item['CLOSE_PRICE']!=None and str(item['CLOSE_PRICE'])!='0':
        FIELDS=[]
        for key,value in item.items():
            if not key in CROSS_REF['LIST'] and key!='CHK_ISIN':
                FIELDS.append(key)
        FIELDS.append("ISO_CURRENCY_CODE")
        #print(FIELDS)
        USING_STR="SELECT "+str(CROSS_REF['CROSS_REF_ID'])+" as CROSS_REF_ID, '"+ dateparser.parse(item['PRICE_DATE']).strftime('%Y-%m-%d')+"' as PRICE_DATE FROM DUAL"
        UPDATE=''
        for i in range(len(FIELDS)):
            key=FIELDS[i]
            if key!='PRICE_DATE' and str(item[key])!='' and str(item[key])!='None' and item[key]!=None and str(item[key])!='0':
                if UPDATE=='':
                    if(('TIME' in key) or ('DATE' in key)):
                        UPDATE=" SET "+key+"=TO_DATE('"+str(item[key])+"','yyyy-mm-dd')"
                    else:
                        UPDATE=" SET "+key+"='"+str(item[key]).replace("'","''")+"'"
                else:
                    if(('TIME' in key) or ('DATE' in key)):
                        UPDATE+=", "+key+"=TO_DATE('"+str(item[key])+"','yyyy-mm-dd')"
                    else:
                        UPDATE+=", "+key+"='"+str(item[key]).replace("'","''")+"'"
        FIELD=""
        VALUES=""
        for i in range(0, len(FIELDS)):
            key=FIELDS[i]
            if str(item[key])!='' and str(item[key])!='None' and item[key]!=None and str(item[key])!='0':
                FIELD+=key+","
                if(('TIME' in key) or ('DATE' in key)):
                    VALUES+="TO_DATE('"+str(item[key])+"','yyyy-mm-dd'),"
                else:
                    VALUES+="'"+str(item[key]).replace("'","''")+"',"
        FIELD+="PRICE_ID,CROSS_REF_ID"
        VALUES+="PRICE_ID_SEQ.NEXTVAL,"+str(CROSS_REF['CROSS_REF_ID'])
        SQL="MERGE INTO WVB_STOCK_PRICE USING ("+USING_STR+")h ON (WVB_STOCK_PRICE.CROSS_REF_ID = h.CROSS_REF_ID AND TO_CHAR(WVB_STOCK_PRICE.PRICE_DATE,'yyyy-mm-dd')=h.PRICE_DATE) WHEN MATCHED THEN UPDATE"+UPDATE+" WHEN NOT MATCHED THEN INSERT ("+FIELD+") VALUES("+VALUES+")"
        #print(SQL)
        RUN=RUNSQL(SQL,conn) 
        return RUN
#---------------------------------------
def Do_INDEX(item,conn):
    item['INDEX_PERM_ID'] = Get_INDEX_PERM_ID_IN_WVB_INDEX_CODES(item['INDEX_MIC'],"INDEX_CODE",item['INDEX_CODE'],conn)
    if item['INDEX_PERM_ID']==0:
        item['INDEX_PERM_ID']=Get_ID('INDEX_PERM_ID',conn)
    FIELDS={"INDEX_CODE","INDEX_SYMBOL","INDEX_DESC","ACTIVE_INACTIVE_FLAG","ISO_COUNTRY_CODE","INDEX_MIC","DATA_SOURCE","DTIME_ENTERED","WHERE_ENTERED","WHO_ENTERED"}
    #print(FIELDS)
    USING_STR="SELECT "+str(item['INDEX_PERM_ID'])+" as INDEX_PERM_ID FROM DUAL"
    UPDATE=''
    for key in FIELDS:
        if str(item[key])!='' and str(item[key])!='None' and item[key]!=None and str(item[key])!='0':
            if UPDATE=='':
                if(('TIME' in key) or ('DATE' in key)):
                    UPDATE=" SET "+key+"=TO_DATE('"+str(item[key])+"','yyyy-mm-dd')"
                else:
                    UPDATE=" SET "+key+"='"+str(item[key]).replace("'","''")+"'"
            else:
                if(('TIME' in key) or ('DATE' in key)):
                    UPDATE+=", "+key+"=TO_DATE('"+str(item[key])+"','yyyy-mm-dd')"
                else:
                    UPDATE+=", "+key+"='"+str(item[key]).replace("'","''")+"'"
    FIELD=""
    VALUES=""
    for key in FIELDS:
        if str(item[key])!='' and str(item[key])!='None' and item[key]!=None and str(item[key])!='0':
            FIELD+=key+","
            if(('TIME' in key) or ('DATE' in key)):
                VALUES+="TO_DATE('"+str(item[key])+"','yyyy-mm-dd'),"
            else:
                VALUES+="'"+str(item[key]).replace("'","''")+"',"
    FIELD+="INDEX_PERM_ID"
    VALUES+=str(item['INDEX_PERM_ID'])
    SQL="MERGE INTO WVB_INDEX_CODES USING ("+USING_STR+")h ON (WVB_INDEX_CODES.INDEX_PERM_ID=h.INDEX_PERM_ID) WHEN MATCHED THEN UPDATE"+UPDATE+" WHEN NOT MATCHED THEN INSERT ("+FIELD+") VALUES("+VALUES+")"
    #print(SQL)
    RUNSQL(SQL,conn)
    # Do Index Weight
    FIELDS={"INDEX_DATE","OPEN_VALUE","CLOSE_VALUE","DAILY_HIGH","DAILY_LOW","VOLUME","VALUE_LOCAL_CURRENCY","HANDLING_CODE","SESS_ID","DTIME_ENTERED","WHERE_ENTERED","WHO_ENTERED","ISO_CURRENCY_CODE"}
    USING_STR="SELECT "+str(item['INDEX_PERM_ID'])+" as INDEX_PERM_ID, '"+item['INDEX_DATE']+"' as INDEX_DATE FROM DUAL"
    UPDATE=''
    for key in FIELDS:
        if str(item[key])!='' and str(item[key])!='None' and item[key]!=None and str(item[key])!='0' and key!='INDEX_DATE':
            if UPDATE=='':
                if(('TIME' in key) or ('DATE' in key)):
                    UPDATE=" SET "+key+"=TO_DATE('"+str(item[key])+"','yyyy-mm-dd')"
                else:
                    UPDATE=" SET "+key+"='"+str(item[key]).replace("'","''")+"'"
            else:
                if(('TIME' in key) or ('DATE' in key)):
                    UPDATE+=", "+key+"=TO_DATE('"+str(item[key])+"','yyyy-mm-dd')"
                else:
                    UPDATE+=", "+key+"='"+str(item[key]).replace("'","''")+"'"
    FIELD=""
    VALUES=""
    for key in FIELDS:
        if str(item[key])!='' and str(item[key])!='None' and item[key]!=None and str(item[key])!='0':
            FIELD+=key+","
            if(('TIME' in key) or ('DATE' in key)):
                VALUES+="TO_DATE('"+str(item[key])+"','yyyy-mm-dd'),"
            else:
                VALUES+="'"+str(item[key]).replace("'","''")+"',"
    FIELD+="INDEX_PERM_ID"
    VALUES+=str(item['INDEX_PERM_ID'])
    SQL="MERGE INTO WVB_INDEX_WEIGHT USING ("+USING_STR+")h ON (WVB_INDEX_WEIGHT.INDEX_PERM_ID = h.INDEX_PERM_ID AND TO_CHAR(WVB_INDEX_WEIGHT.INDEX_DATE,'yyyy-mm-dd')=h.INDEX_DATE) WHEN MATCHED THEN UPDATE"+UPDATE+" WHEN NOT MATCHED THEN INSERT ("+FIELD+") VALUES("+VALUES+")"
    #print(SQL)
    RUN=RUNSQL(SQL,conn)
    return RUN
