import pandas as pd
import streamlit as sl


sl.set_page_config(page_title='Crypto Panda',page_icon=":panda_face")
sl.title("Crypto Panda 🐼")
sl.header("Hi 👋 i am Crypto Panda, I will teach you about Cryptos in a useful and fun way")
sl.header("                                                  ")

sl.image('cryp.jpeg',use_column_width=True)   
Stocklist=['ADA(Cardano)','Dogecoin','Litecoin','Etherum','Bitcoin']

if(sl.checkbox("Select Crypto")):
    stockChosen=sl.multiselect('Select a stock',Stocklist)
    if (stockChosen==[]):
        sl.error("Warning : Please choose a Crypto")    
    
    elif(len(stockChosen)>=2):
        sl.error("Warning :Please Choose Only one at a time")
    
    elif(stockChosen[0]==Stocklist[0]):
        df=pd.read_csv('ADA-USD.csv')
        df.rename(columns={'Date': 'Day'},inplace=True)
        dlen=len(df)
        for i in range(0,dlen):
            df['Day'][i]=i+1
        mean=df['Close'].mean()    
        df.fillna(value=mean,inplace=True)   

        sl.image('ada.jpg',use_column_width=True)  
        sl.warning("NOTE : Cryptos tend to fluctuate quickly so kindly invest in them at your own risk")
        sl.info("By clicking the checkbox below you can view the data by which the model has been trained")
        if(sl.checkbox("Show Data")):
            sl.write("Below are the data of Cryptos ")
            sl.dataframe(df)
        if(sl.checkbox("Meaningful data representation")):
            sl.markdown("**Insights** of the data ")
            basicInfo=df.describe()
            sl.dataframe(basicInfo)
            sl.markdown("*Bar graph*")
            sl.bar_chart(basicInfo)
        sl.video('Analysis.mp4') 
        from sklearn.ensemble import RandomForestRegressor
        X=df.iloc[:, 0].values
        X=X.reshape(dlen,1)
        Y=df.iloc[:, [1,4]].values
        from sklearn.model_selection import train_test_split
        X_train,X_test,Y_train,Y_test=train_test_split(X,Y)
        model=RandomForestRegressor(n_estimators=19)
        model.fit(X_train,Y_train)
        pred=model.predict(X_test)
        sl.markdown('**Sample Predictions**')
        sl.line_chart(pred[0:150])
        Day=1
        PreVal=X.shape[0]
        sl.markdown("**Play** with the model yourself to **Predict**")
        sl.markdown(' With the **Slider** given below choose which day from today you want to predict ')
        sl.slider('Day',min_value=1,max_value=30)
        predicted=model.predict([[Day+PreVal]])
        sl.write("The Predicted opening price and closing price of Cryptos are ",predicted)
    
    elif(stockChosen[0]==Stocklist[1]):
        sl.title("🐕 Dogecoin")
        df=pd.read_csv('DOGE-USD.csv')
        df.rename(columns={'Date': 'Day'},inplace=True)
        dlen=len(df)
        for i in range(0,dlen):
            df['Day'][i]=i+1
        mean=df['Close'].mean()    
        df.fillna(value=mean,inplace=True)   

        sl.image('DogeCoin.jpg',use_column_width=True)  
        sl.warning("NOTE : Cryptos tend to fluctuate quickly so kindly invest in them at your own risk")
        sl.info("By clicking the checkbox below you can view the data by which the model has been trained")
        if(sl.checkbox("Show Data")):
            sl.write("Below are the data of Cryptos ")
            sl.dataframe(df)
        if(sl.checkbox("Meaningful data representation")):
            sl.markdown("**Insights** of the data ")
            basicInfo=df.describe()
            sl.dataframe(basicInfo)
            sl.markdown("*Bar graph*")
            sl.bar_chart(basicInfo)
        sl.video('Analysis.mp4') 
        from sklearn.ensemble import RandomForestRegressor
        X=df.iloc[:, 0].values
        X=X.reshape(dlen,1)
        Y=df.iloc[:, [1,4]].values
        from sklearn.model_selection import train_test_split
        X_train,X_test,Y_train,Y_test=train_test_split(X,Y)
        model=RandomForestRegressor(n_estimators=19)
        model.fit(X_train,Y_train)
        pred=model.predict(X_test)
        sl.markdown('**Sample Predictions**')
        sl.line_chart(pred[0:150])
        Day=1
        PreVal=X.shape[0]
        sl.markdown("**Play** with the model yourself to **Predict**")
        sl.markdown(' With the **Slider** given below choose which day from today you want to predict ')
        sl.slider('Day',min_value=1,max_value=30)
        predicted=model.predict([[Day+PreVal]])
        sl.write("The Predicted opening price and closing price of Cryptos are ",predicted)

    
    elif(stockChosen[0]==Stocklist[4]):
        sl.title("₿ Bitcoin")
        df=pd.read_csv('BTC-USD.csv')
        df.rename(columns={'Date': 'Day'},inplace=True)
        dlen=len(df)
        for i in range(0,dlen):
            df['Day'][i]=i+1
        mean=df['Close'].mean()    
        df.fillna(value=mean,inplace=True)   

        sl.warning("NOTE : Cryptos tend to fluctuate quickly so kindly invest in them at your own risk")
        sl.info("By clicking the checkbox below you can view the data by which the model has been trained")
        if(sl.checkbox("Show Data")):
            sl.write("Below are the data of Cryptos ")
            sl.dataframe(df)
        if(sl.checkbox("Meaningful data representation")):
            sl.markdown("**Insights** of the data ")
            basicInfo=df.describe()
            sl.dataframe(basicInfo)
            sl.markdown("*Bar graph*")
            sl.bar_chart(basicInfo)
        sl.video('Analysis.mp4') 
        from sklearn.ensemble import RandomForestRegressor
        X=df.iloc[:, 0].values
        X=X.reshape(dlen,1)
        Y=df.iloc[:, [1,4]].values
        from sklearn.model_selection import train_test_split
        X_train,X_test,Y_train,Y_test=train_test_split(X,Y)
        model=RandomForestRegressor(n_estimators=19)
        model.fit(X_train,Y_train)
        pred=model.predict(X_test)
        sl.markdown('**Sample Predictions**')
        sl.line_chart(pred[0:150])
        Day=1
        PreVal=X.shape[0]
        sl.markdown("**Play** with the model yourself to **Predict**")
        sl.markdown(' With the **Slider** given below choose which day from today you want to predict ')
        sl.slider('Day',min_value=1,max_value=30)
        predicted=model.predict([[Day+PreVal]])
        sl.write("The Predicted opening price and closing price of Cryptos are ",predicted)

    elif(stockChosen[0]==Stocklist[3]):
        sl.title("⧫ Ethereum")
        df=pd.read_csv('ETH-USD.csv')
        df.rename(columns={'Date': 'Day'},inplace=True)
        dlen=len(df)
        for i in range(0,dlen):
            df['Day'][i]=i+1
        mean=df['Close'].mean()    
        df.fillna(value=mean,inplace=True)   

        sl.warning("NOTE : Cryptos tend to fluctuate quickly so kindly invest in them at your own risk")
        sl.info("By clicking the checkbox below you can view the data by which the model has been trained")
        if(sl.checkbox("Show Data")):
            sl.write("Below are the data of Cryptos ")
            sl.dataframe(df)
        if(sl.checkbox("Meaningful data representation")):
            sl.markdown("**Insights** of the data ")
            basicInfo=df.describe()
            sl.dataframe(basicInfo)
            sl.markdown("*Bar graph*")
            sl.bar_chart(basicInfo)
        sl.video('Analysis.mp4') 
        from sklearn.ensemble import RandomForestRegressor
        X=df.iloc[:, 0].values
        X=X.reshape(dlen,1)
        Y=df.iloc[:, [1,4]].values
        from sklearn.model_selection import train_test_split
        X_train,X_test,Y_train,Y_test=train_test_split(X,Y)
        model=RandomForestRegressor(n_estimators=19)
        model.fit(X_train,Y_train)
        pred=model.predict(X_test)
        sl.markdown('**Sample Predictions**')
        sl.line_chart(pred[0:150])
        Day=1
        PreVal=X.shape[0]
        sl.markdown("**Play** with the model yourself to **Predict**")
        sl.markdown(' With the **Slider** given below choose which day from today you want to predict ')
        sl.slider('Day',min_value=1,max_value=30)
        predicted=model.predict([[Day+PreVal]])
        sl.write("The Predicted opening price and closing price of Cryptos are ",predicted)
    
    elif(stockChosen[0]==Stocklist[2]):
        sl.title("I❣ Litecoin")
        df=pd.read_csv('LTC-USD.csv')
        df.rename(columns={'Date': 'Day'},inplace=True)
        dlen=len(df)
        for i in range(0,dlen):
            df['Day'][i]=i+1
        mean=df['Close'].mean()    
        df.fillna(value=mean,inplace=True)   

        sl.image('Litecoin.jpg',use_column_width=True)  
        sl.warning("NOTE : Cryptos tend to fluctuate quickly so kindly invest in them at your own risk")
        sl.info("By clicking the checkbox below you can view the data by which the model has been trained")
        if(sl.checkbox("Show Data")):
            sl.write("Below are the data of Cryptos ")
            sl.dataframe(df)
        if(sl.checkbox("Meaningful data representation")):
            sl.markdown("**Insights** of the data ")
            basicInfo=df.describe()
            sl.dataframe(basicInfo)
            sl.markdown("*Bar graph*")
            sl.bar_chart(basicInfo)
        sl.video('Analysis.mp4') 
        from sklearn.ensemble import RandomForestRegressor
        X=df.iloc[:, 0].values
        X=X.reshape(dlen,1)
        Y=df.iloc[:, [1,4]].values
        from sklearn.model_selection import train_test_split
        X_train,X_test,Y_train,Y_test=train_test_split(X,Y)
        model=RandomForestRegressor(n_estimators=19)
        model.fit(X_train,Y_train)
        pred=model.predict(X_test)
        sl.markdown('**Sample Predictions**')
        sl.line_chart(pred[0:150])
        Day=1
        PreVal=X.shape[0]
        sl.markdown("**Play** with the model yourself to **Predict**")
        sl.markdown(' With the **Slider** given below choose which day from today you want to predict ')
        sl.slider('Day',min_value=1,max_value=30)
        predicted=model.predict([[Day+PreVal]])
        sl.write("The Predicted opening price and closing price of Cryptos are ",predicted)



if(sl.button("About this app")):
    sl.info("This webapp is still under construction and works with a machine learning model behind it ")
if(sl.button("Version")):
    sl.info("Version:0.3")  
myRate=sl.sidebar.slider("Stars 🌟 for me 🥺",max_value=5,min_value=1)

    
