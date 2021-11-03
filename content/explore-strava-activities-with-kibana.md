Title: Exploring my own Strava activities using Kibana
Date: 2021-11-03 09:00
Tags: dataviz data visualisation
Slug: explore-strava-activities-with-kibana
Author: Nicolas Kosinski
Summary: Use Kibana to explore my personal Sport activities from strava.com
Lang: en

Assumed audience: people interested in data exploration.

# Exploring my own Strava activities using Kibana

I use [strava.com](https://strava.com/) to track my running/hike activities since a few years. Since Strava provides an API to export my activities, I had a try exploring them via a data visualization tool, [Kibana](https://www.elastic.co/kibana/). This article relates my first exploration.


## Setup

Note that the code shown below uses `zsh` Unix shell. 

### Grab Strava activities

1. First step, create a [Strava developer account](https://developers.strava.com/docs/getting-started/#account), then create a Strava API OAuth2 access token (I have used the [mgryszko/strava-access-token generator](https://github.com/mgryszko/strava-access-token)).

2. Second step, use [the Strava API to grab my Strava activities](https://developers.strava.com/docs/reference/#api-Activities-getLoggedInAthleteActivities), exporting all activities into separate JSON files:

```zsh
for page in {1..10}; http GET "https://www.strava.com/api/v3/athlete/activities?include_all_efforts=&per_page=200&page=${page}" "Authorization: Bearer $TOKEN" > strava-activities-${page}.json
```

Since I have recorded around 300 activities with Strava, only three files have a non-empty content (empty JSON content is `[]`), as seen with the `wc` command:

```zsh
wc -c strava-activities-*.json

  421462 strava-activities-1.json
       2 strava-activities-10.json
  288391 strava-activities-2.json
   57159 strava-activities-3.json
       2 strava-activities-4.json
       2 strava-activities-5.json
       2 strava-activities-6.json
       2 strava-activities-7.json
       2 strava-activities-8.json
       2 strava-activities-9.json
  767026 total
```

3. Third step, aggregate files into a single "Newline Delimited JSON" file (`ndjson` extension):

```zsh
for n in {1..3}; cat strava-activities-${n}.json | jq -c '.[]' > strava-activities-${n}.ndjson
cat strava-activities-1.ndjson strava-activities-2.ndjson strava-activities-3.ndjson >> strava-activities.ndjson
```

### Insert data into Kibana

We will run Elastic and Kibana using the [official Docker images](https://www.elastic.co/guide/en/kibana/current/docker.html).

1. Start Elastic and Kibana:

```sh
docker network create elastic
docker run --name es-dataviz --net elastic --publish 9200:9200 --publish 9300:9300 --env "discovery.type=single-node" --env "xpack.security.enabled=false" docker.elastic.co/elasticsearch/elasticsearch:7.15.1
```

```sh
docker run --name kb-dataviz --net elastic --publish 5601:5601 --env "ELASTICSEARCH_HOSTS=http://es-dataviz:9200" --env "xpack.security.enabled=false" docker.elastic.co/kibana/kibana:7.15.1
```

2. Upload `ndjson` file [http://localhost:5601/app/home#/tutorial_directory] into a `strava` index:

Open Kibana's "discover" view for the last 6 years:
<img alt="Discover Kibana" src="images/explore-strava-discover.png">

## Explore data / create dashboards

### Average speed per activity


Let's create a dashboard to visualize the activities' average speed by activity type (run, hike etc.):

<img alt="Create Kibana dashboard" src="images/explore-strava-create-dashboard.png">

It looks like this:

<img width="1436" alt="Create Kibana dashboard" src="images/explore-strava-dashboard.png">

That's all! I'll try to go further an other time. 🤓
