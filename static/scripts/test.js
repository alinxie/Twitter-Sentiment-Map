var error = function (err, response, body) {
    console.log('ERROR [%s]', err);
};
var success = function (data) {
    //console.log('Data is ' + data);
    data = JSON.parse(data);
    //console.log("statuses is "+ data.statuses);
    for (var i = 0; i< data.statuses.length; i++) {
      console.log(data.statuses[i].text);
    }

};


var Twitter = require('twitter-node-client').Twitter;

var config ={
    "consumerKey": "8wCShnmuYrOZYSZlal2SPOLLR",
    "consumerSecret": "fQ6p2d9d1W1rANipq9wQ81qFDRNdgDx1hjuiKma5PtD1ujeKAs",
    "accessToken": "338743525-lFE1f3YTFYpUWQCj6FHsafPh1ISjxHVltZtjsmxp",
    "accessTokenSecret": "1qc2UdUNR4EZnc889NOEuC4mLUxpq6ZLJzSyBqobEy9VJ",
    "callBackUrl": "http://github.com/c0dyzeng"
}

var twitter = new Twitter(config);


twitter.getSearch({'q':'#trump','count': 10}, error, success);
