import griddb_python as griddb
import pandas as pd
factory = griddb.StoreFactory.get_instance()
# Initialize container
try:
    gridstore = factory.get_store(host=your_host, port=ypur_port, 
            cluster_name=your_cluster_name, username=your_username, 
            password=your_password)
conInfo = griddb.ContainerInfo("Phishing Websites",
                    [              
                     ["having_IP_Address", griddb.Type.INTEGER],
                     ["URL_Length", griddb.Type.INTEGER],
                     ["Shortining_Service", griddb.Type.INTEGER],
                     ["having_At_Symbol", griddb.Type.INTEGER],
                     ["double_slash_redirecting", griddb.Type.INTEGER],
                     ["Prefix_Suffix", griddb.Type.INTEGER],
                     ["having_Sub_Domain", griddb.Type.INTEGER],
                     ["SSLfinal_State", griddb.Type.INTEGER],
                     ["Domain_registeration_length", griddb.Type.INTEGER],
                     ["Favicon", griddb.Type.INTEGER],
                     ["port", griddb.Type.INTEGER],
                     ["HTTPS_token", griddb.Type.INTEGER],
                     ["Request_URL", griddb.Type.INTEGER],
                     ["URL_of_Anchor", griddb.Type.INTEGER],
                     ["Links_in_tags", griddb.Type.INTEGER],
                     ["SFH", griddb.Type.INTEGER],
                     ["Submitting_to_email", griddb.Type.INTEGER],
                     ["Abnormal_URL", griddb.Type.INTEGER],
                     ["Redirect", griddb.Type.INTEGER],
                     ["on_mouseover", griddb.Type.INTEGER],
                     ["RightClick", griddb.Type.INTEGER],
                     ["popUpWidnow", griddb.Type.INTEGER],
                     ["Iframe", griddb.Type.INTEGER],
                     ["age_of_domain", griddb.Type.INTEGER],
                     ["DNSRecord", griddb.Type.INTEGER],
                     ["web_traffic", griddb.Type.INTEGER],
                     ["Page_Rank", griddb.Type.INTEGER],
                     ["Google_Index", griddb.Type.INTEGER],
                     ["Links_pointing_to_page", griddb.Type.INTEGER],
                     ["Statistical_report", griddb.Type.INTEGER],
                     ["Result", griddb.Type.INTEGER],                    
                    ],
                    griddb.ContainerType.COLLECTION, True)
    cont = gridstore.put_container(conInfo)   
   # cont.create_index("id", griddb.IndexType.DEFAULT)
    data = pd.read_csv("dataset.csv")
    #Add data
    for i in range(len(data)):
        ret = cont.put(data.iloc[i, :])
    print("Successfully added the data")
except griddb.GSException as e:
    for i in range(e.get_error_stack_size()):
        print("[", i, "]")
        print(e.get_error_code(i))
        print(e.get_location(i))
        print(e.get_message(i))
sql_statement = ('SELECT * FROM Ocean_Data')
sql_query = pd.read_sql_query(sql_statement, cont)

























