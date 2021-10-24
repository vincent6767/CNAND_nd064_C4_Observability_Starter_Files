**Note:** For the screenshots, you can store all of your answer images in the `answer-img` directory.

## Verify the monitoring installation

*TODO:* run `kubectl` command to show the running pods and services for all components. Take a screenshot of the output and include it here to verify the installation

* You can access the result images in **answer-img/all-resources-running** folder

## Setup the Jaeger and Prometheus source
*TODO:* Expose Grafana to the internet and then setup Prometheus as a data source. Provide a screenshot of the home page after logging into Grafana.

* You can access the Grafana Homepage image in **answer-img/grafana-homepage.png**

## Create a Basic Dashboard
*TODO:* Create a dashboard in Grafana that shows Prometheus as a source. Take a screenshot and include it here.

* You can access the Grafana Dashboard with Prometheus as a source in **answer-img/grafana-dashboard-with-prometheus-ds**

## Describe SLO/SLI
*TODO:* Describe, in your own words, what the SLIs are, based on an SLO of *monthly uptime* and *request response time*.

* Service Level Indicators (SLI) are incidators / metrics used to measure the performance of a service. **It's an actual measurement** to show whether the team **achieved the SLO or not**. So for example,
    
    * The team set *monthly service uptime to be 99.9%* as a SLO. The SLI is the actual percentage of minutes in a given month.
    * The team set *service request response time* as 500ms as a SLO. The SLI is the actual response time for each specific requests.

## Creating SLI metrics.
*TODO:* It is important to know why we want to measure certain metrics for our customer. Describe in detail 5 metrics to measure these SLIs.

   * There are many metrics that could be used to measure SLIs. But most of them could be categorized into 4 metrics, called golden signals. Those are:
        * **Latency**: The time taken to serve a request (usually measured in ms).
        * **Traffic**: The amount of stress on a system from demand (such as the number of HTTP requests/second)
        * **Saturation**: The overall capacity of a service (such as the percentage of memory or CPU used)
        * **Errors**: The number of requests that are failing (such as number of HTTP 500 responses).

## Create a Dashboard to measure our SLIs
*TODO:* Create a dashboard to measure the uptime of the frontend and backend services We will also want to measure to measure 40x and 50x errors. Create a dashboard that show these values over a 24 hour period and take a screenshot.

## Tracing our Flask App
*TODO:*  We will create a Jaeger span to measure the processes on the backend. Once you fill in the span, provide a screenshot of it here.

## Jaeger in Dashboards
*TODO:* Now that the trace is running, let's add the metric to our current Grafana dashboard. Once this is completed, provide a screenshot of it here.

* You can see the image in **answer-img/jaeger-traces-grafana.png**

## Report Error
*TODO:* Using the template below, write a trouble ticket for the developers, to explain the errors that you are seeing (400, 500, latency) and to let them know the file that is causing the issue.

TROUBLE TICKET

Name: 500 Internal server error on /star endpoint

Date: October 24th, 2021

Subject: "Add star" functionality returns 500 internal server error

Affected Area: Add star functionality (backend)

Severity: Critical, functionality can't be accessed

Description: Users are blocked completely to add star features due error. Here is the trace ID for further information including the error log: **595b76dd18bf0b74**



## Creating SLIs and SLOs
*TODO:* We want to create an SLO guaranteeing that our application has a 99.95% uptime per month. Name three SLIs that you would use to measure the success of this SLO.

## Building KPIs for our plan
*TODO*: Now that we have our SLIs and SLOs, create KPIs to accurately measure these metrics. We will make a dashboard for this, but first write them down here.

## Final Dashboard
*TODO*: Create a Dashboard containing graphs that capture all the metrics of your KPIs and adequately representing your SLIs and SLOs. Include a screenshot of the dashboard here, and write a text description of what graphs are represented in the dashboard.  
