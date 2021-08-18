## Tracking Transaction Life Cycles via SMS 📱

While dApps on Ethereum have become incredibly complex, one of the largest pain points for Ethereum users is the lack of transparency and clarity surrounding a transaction's life cycle. Oftentimes, dApp users are left with uncertainty surrounding pending transactions, forcing them to constantly refresh block explorers or their wallet dashboards to check if their transactions have been confirmed/mined. 

### Problem Statement: ###
For dApps, simple notifications that track transaction life cycles provide a valuable user experience that allows for higher customer engagement, helping to alleviate the stress involved in pending transactions as Ethereum's ever-increasing gas fees force users to set lower `maxPriorityFeePerGas` to save money and inadvertently increase wait times. While building reliable transaction trackers has traditionally been complicated and unreliable, Alchemy Notify and Alchemy's pending transaction WebSocket allows us to monitor and send sending real-time push notifications regarding tx life cycles.  

***
In this tutorial, we’ll look at an example of how, with just a few lines of code, your dApp can integrate the power of Alchemy's Enhanced API suite, leveraging multiple Alchemy products to build a single feature to enhance user experience.


### 🚀 Launching with Heroku ###

 1. Get the repo!

      * `https://github.com/alchemyplatform/Alchemy-Transfers-Tutorial`

For all Heroku dependent documentation, refer to:
https://devcenter.heroku.com/articles/getting-started-with-nodejs?singlepage=true 
for more detailed instructions.  The Heroku instructions included below are abridged.

 2. Install Heroku-CLI and verify/install dependencies.

      * Download Heroku-CLI based on your OS [https://devcenter.heroku.com/articles/heroku-cli]
      * After installation, open your terminal and run `heroku login`; follow the commands that follow to login to your Heroku account.  If you don't have a Heroku account, you can [sign up for one](https://dashboard.heroku.com/apps)!
      * Run `node --version`.  You may have any version of Node greater than 10.  If you don’t have it or have an older version, install a more recent version of Node.
      * Run `npm --version`.  `npm` is installed with Node, so check that it’s there. If you don’t have it, install a more recent version of Node:
      * Run `git --version`   Check to make sure you have git installed.  

 3. Initiate Heroku.
 
      * Run `heroku create` to create your heroku app. Take note of the info that pops up in the terminal, especially the URL that looks like  http://xxxxxxxxx.herokuapp.com/ That's the URL for your dashboard!

 3. Add in your Alchemy API Key.

      > Change the Alchemy API Key in `main.py` to reflect your particular Alchemy auth token!  We recommend that you set this key in your environment variables. 
       
To set the API key in Heroku's environment variables, run: `heroku config:set KEY="<YOUR ALCHEMY KEY>"`
      
Don't forget to sign into your Alchemy account to use the Transfers API.  See https://docs.alchemy.com/alchemy/documentation/apis/enhanced-apis/transfers-api for more specific documentation.  

If you don’t already have an Alchemy account, [you’ll first need to create one](https://alchemy.com/?r=affiliate:ba2189be-b27d-4ce9-9d52-78ce131fdc2d). The free version will work fine for getting started.  First, we create an App for our Dashboard by clicking “Create App” under the Apps dropdown menu.

![webhook_1](https://github.com/pileofscraps/Alchemy-Transfers-Tutorial/blob/master/app.png)
      
Once we have created the app and pointed it towards the appropriate network, we're ready to go and can paste in our key.

 4. Deploy Heroku.

      * Run `git add .`
      * Run `git commit -m "added Alchemy keys"`
      * Run `git push heroku master` to push and deploy your heroku app.
     
🎉 Congratulations on your dApp deployment! Feel free to edit your app, change its behavior, or make the frontend more spiffy!
