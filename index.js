require("dotenv").config({ path: __dirname + "/.env" });
const { twitterClient } = require("./twitterClient.js");
const CronJob = require("cron").CronJob;
const fs = require('fs');

let uncScore
let awayTeamScore

fs.readFile('data.json', 'utf8', (err, data) => {
    if (err) {
        console.error(err);
        return;
    }

    const jsonData = JSON.parse(data);

    uncScore = jsonData.unc_score;
    awayTeamScore = jsonData.awayteam_score;
  });

const tweet = async () => {
    const time = new Date().getTime();
    const date = new Date(time);

  try {
    await twitterClient.v2.tweet("UNC: " + uncScore + ", AwayTeam: " + awayTeamScore + " - " + date);
  } catch (e) {
    console.log(e)
  }
}

const cronTweet = new CronJob("30 * * * * *", () => { 
    tweet().catch(error => console.error(error));
});

  
cronTweet.start();

//tweet();