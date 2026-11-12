# NHS Waiting List Backlog Forecasting

## Final Project Submission

## 1. Executive Summary

This project applies time-series forecasting to examine waiting-list pressure in the NHS, focusing on incomplete Referral to Treatment (RTT) pathways in the Trauma and Orthopaedics specialty at Lancashire Teaching Hospitals NHS Foundation Trust. Using 43 monthly observations from NHS England, covering January 2023 to July 2026, the project investigates how the backlog has evolved and estimates its potential trajectory over the following six months. The first 36 observations were used for model training, while January to July 2026 formed the holdout test period.

The analysis found that incomplete pathways increased from 3,301 in January 2023 to 4,771 in July 2026, representing a 44.5% increase. The backlog also increased between May and July in each of the four observed years, suggesting a possible recurring pattern of pressure during these months, although the limited historical period and underlying upward trend make it difficult to establish seasonality conclusively. Meanwhile, the average monthly number of pathways waiting 52 weeks or longer declined from approximately 156 in 2023 to 24 during January–July 2026. No pathways waiting 78 weeks or longer were recorded from 2025 onwards. This indicates that growth in the overall waiting list has not been accompanied by a similar increase in the longest-waiting categories.

Four baseline forecasting approaches were compared alongside ARIMA and SARIMA models. The Naive model achieved the lowest holdout test Mean Absolute Error (MAE) of 105.7 pathways. Standard ARIMA produced the same result, while ARIMA with drift recorded an MAE of 109.4 and SARIMA 283.3. Although SARIMA performed better during time-series cross-validation, achieving an MAE of 150.1 compared with 205.7 for the Naive model, this advantage was not replicated on the most recent holdout period. The Naive model was therefore selected for the final forecast based on its performance on the held-out data and its simplicity.

Using the complete historical dataset, the selected model forecasts 4,771 incomplete pathways per month from August 2026 to January 2027. This flat projection reflects the model's assumption that the latest observed backlog will persist. To communicate uncertainty, 80% and 95% prediction intervals were generated. The 95% interval widens from approximately 4,499–5,043 pathways in August 2026 to 4,105–5,437 in January 2027. The January 80% upper bound is approximately 5,207 pathways. These estimates provide a range of possible backlog levels that can inform monitoring and planning, rather than a precise measure of future treatment requirements.

From a service-planning perspective, the findings highlight the importance of monitoring both the overall backlog and the distribution of waiting times. The sustained increase in incomplete pathways suggests continued pressure on elective care, even as the number of patients experiencing extremely long waits has declined. The flat forecast should therefore be interpreted cautiously: it does not capture the historical upward trend or the possible recurring May–July increases. Actual backlog levels could exceed the point forecast if the factors contributing to previous growth persist.

A key limitation is that the analysis forecasts incomplete pathways only. It does not model incoming referrals, admitted and non-admitted treatment activity, staffing levels or available clinical capacity. Consequently, it cannot independently determine how many additional treatments, clinical sessions or staff would be required to reduce the backlog. The forecast should be updated as new monthly data becomes available, with actual outcomes compared against predictions and model performance reassessed.

## 2. Problem Statement and Objectives

Waiting times for elective healthcare remain an important operational challenge for the NHS. NHS England publishes monthly Referral to Treatment (RTT) statistics, providing information on patients waiting for treatment across healthcare providers and clinical specialties. However, historical reporting describes how waiting lists have changed; it does not, by itself, provide an estimate of how waiting-list backlogs might develop in the future.

For NHS providers, understanding the potential trajectory of incomplete RTT pathways is important for monitoring service pressure and informing decisions about elective care planning. This is particularly relevant to specialties such as Trauma and Orthopaedics, where managing the volume and duration of patient waits requires ongoing attention.

This project applies time-series forecasting to monthly incomplete RTT pathways in the Trauma and Orthopaedics specialty at Lancashire Teaching Hospitals NHS Foundation Trust. Using 43 monthly observations from NHS England, covering January 2023 to July 2026, it examines historical backlog patterns, evaluates alternative forecasting models and generates a six-month forecast for August 2026 to January 2027. Prediction intervals are also used to communicate the uncertainty surrounding the forecast.

The central aim is to determine whether historical incomplete pathway data can provide a useful baseline for anticipating future waiting-list volumes and supporting more informed monitoring and planning.

The project addresses the following research and analytical questions:

1. How has the incomplete RTT pathway backlog changed between January 2023 and July 2026?
2. Are there recurring monthly patterns that may indicate seasonality?
3. How does a simple forecasting baseline perform compared with more advanced time-series models?
4. What backlog levels does the selected model project over the following six months?
5. How uncertain are these forecasts, and how well have the prediction intervals performed against historical observations?
6. How can the forecast and its uncertainty inform waiting-list monitoring and capacity-planning discussions?
7. What assumptions and data limitations could affect the reliability and practical interpretation of the results?

**Scope:** The analysis focuses on one NHS provider and one treatment function: Lancashire Teaching Hospitals NHS Foundation Trust (RXN), Trauma and Orthopaedics (C_110). The target variable is the monthly number of incomplete RTT pathways, representing the active waiting-list backlog rather than new referrals or total patient demand. Forecasting models are evaluated using time-based holdout testing and cross-validation. The modelling does not incorporate new referrals, completed treatment activity, staffing or available clinical capacity. Therefore, it provides a baseline projection of backlog volumes rather than a direct estimate of future treatment demand or the additional resources required to reduce waiting times.

## 3. Data Sources and Preparation

The data used in this project was obtained from NHS England's [Referral to Treatment (RTT) waiting-times statistics](https://www.england.nhs.uk/statistics/statistical-work-areas/rtt-waiting-times/).

The analysis uses the monthly provider-level **Incomplete Pathways** datasets. These datasets report the number of patients whose RTT pathways remain open at the end of each reporting month, providing a measure of the active waiting-list backlog.

Monthly Excel workbooks were downloaded individually, covering January 2023 to July 2026. This produced 43 source files, named using the convention `incomplete_provider_<month>_<year>`.

The source files were published in two Excel formats. Forty-two workbooks used the `.xlsx` format, while the April 2023 workbook (`incomplete_provider_april_2023.xls`) used the older `.xls` format. The data-loading process was designed to accommodate both extensions.

### 3.2 Combining and Processing the Files

A Python data-processing script was developed to automate the loading and preparation of the monthly workbooks.

Each workbook was read and passed through a shared data-wrangling function. This function standardised the structure of the extracted data and added a `period` column representing the corresponding reporting month, derived from the source filename.

After processing, each monthly dataset was exported as an individual CSV file. The 43 processed CSV files were subsequently combined into a single dataset, creating a consolidated monthly record of provider-level RTT incomplete pathways.

The resulting dataset contains observations across providers and treatment functions for each reporting month. This consolidated structure made it possible to filter the data by provider, treatment function and reporting period for subsequent exploratory analysis and forecasting.

### 3.3 Selection of Provider and Treatment Function

The project focuses on Lancashire Teaching Hospitals NHS Foundation Trust, identified by provider code `RXN`, and Trauma and Orthopaedics, identified by Treatment Function Code `C_110`.

This provider–specialty combination was selected to establish a manageable forecasting scope while retaining sufficient historical observations for time-series analysis.

The target variable is the **Total number of incomplete pathways**. This represents the number of active RTT pathways at the end of each reporting month and is treated as a measure of waiting-list backlog rather than new referrals or incoming patient demand.

Filtering the consolidated dataset to this provider and treatment function produced 43 monthly observations, covering January 2023 to July 2026. This series was used for the subsequent exploratory data analysis, model development and forecasting.

## 4. Exploratory Data Analysis

This section examines the historical behaviour of incomplete RTT pathways before model development. The analysis focuses on the overall backlog trend, month-to-month fluctuations, recurring monthly patterns, waiting-time indicators and the distribution of long-waiting pathways. These observations help establish the characteristics of the series and inform the selection and evaluation of forecasting models.

### 4.1 Incomplete Pathways per Month (Figure 1)

Figure 1 shows the monthly number of incomplete RTT pathways for Trauma and Orthopaedics at Lancashire Teaching Hospitals NHS Foundation Trust from January 2023 to July 2026.

The series shows a general upward trend, increasing from 3,301 pathways in January 2023 to 4,771 in July 2026, representing a 44.5% increase. This indicates a sustained increase in the size of the active waiting list and suggests growing pressure on the service.

Although month-to-month movements are uneven, a recurring pattern is visible between May and July. In each of the four observed years, incomplete pathways increased consecutively across these three months.

| Year |   May |  June |  July |
| ---- | ----: | ----: | ----: |
| 2023 | 3,268 | 3,465 | 3,679 |
| 2024 | 3,534 | 3,601 | 3,725 |
| 2025 | 3,908 | 4,032 | 4,084 |
| 2026 | 4,447 | 4,561 | 4,771 |

This repeated increase may indicate a recurring period of waiting-list pressure. However, the observation alone does not establish annual seasonality. The underlying upward trend may also contribute to the increases, and further observations would be needed to establish whether this pattern is seasonal.

### 4.2 Month-on-Month Percentage Change (Figure 2)

Figure 2 examines the percentage change in incomplete pathways between consecutive months. The series contains both positive and negative movements, although positive changes occur more frequently. This is consistent with the overall upward trend observed in the backlog.

The largest monthly increase and decrease both occurred in 2025:

- **Largest decrease:** March 2025 recorded a fall of approximately 6.0%, from 4,114 pathways in February to 3,867 in March.
- **Largest increase:** September 2025 recorded an increase of approximately 9.78%, from 4,060 pathways in August to 4,457 in September.

These movements represent the most pronounced month-to-month changes identified in the series. They are worth investigating as potential unusual observations, but the available data does not establish their causes. Changes in referrals, treatment activity, operational circumstances or reporting may have contributed.

### 4.3 Yearly Comparison and Recurring Patterns (Figure 3)

Figure 3 provides a year-by-year comparison of incomplete RTT pathways. The overall pattern supports the upward movement observed in the monthly series, with later years generally recording higher backlog levels than earlier years.

However, 2026 contains observations only from January to July, whereas 2023, 2024 and 2025 cover complete calendar years. Consequently, comparing full-year totals would not provide a fair comparison. The 2026 figures should be compared with January–July figures from previous years, or the chart should use monthly averages calculated over equivalent reporting periods.

The year-by-year comparison provides further context for the growth in the waiting list, but it should not be interpreted as independent evidence of seasonality. The recurring May–July increases identified in Figure 1 provide the more direct observation of a possible seasonal pattern.

### 4.4 Average Monthly Median Waiting Time (Figure 4)

Figure 4 examines changes in the median waiting time of incomplete RTT pathways. The average of the monthly median waiting-time values increased across the observed years:

| Year                | Average monthly median waiting time (weeks) |
| ------------------- | ------------------------------------------: |
| 2023                |                                       12.40 |
| 2024                |                                       13.14 |
| 2025                |                                       14.45 |
| 2026 (January–July) |                                       15.78 |

This indicates that the average monthly median waiting time increased over the period, although the 2026 figure covers only seven months.

Within individual years, the monthly median waiting time also fluctuated. One notable movement occurred in 2025, when the monthly median fell from 15.9 weeks in September to 10.7 weeks in November.

Another recurring observation is that median waiting times generally declined between March and June in 2023, 2024 and 2025. In 2026, the direction over the same period was different, with waiting times increasing.

These observations suggest that changes in the overall backlog and changes in the distribution of waiting times do not necessarily move together. The monthly median provides a summary of the waiting-time distribution; it does not mean that every patient's waiting time increased or decreased by the same amount.

### 4.5 Long-Waiting Pathways (Figure 5)

Figure 5 compares the average monthly number of incomplete pathways waiting 52 weeks or longer, 65 weeks or longer, and 78 weeks or longer.

| Waiting-time threshold |   2023 |  2024 |  2025 | 2026\* |
| ---------------------- | -----: | ----: | ----: | -----: |
| 52+ weeks              | 156.25 | 52.58 | 36.25 |  24.14 |
| 65+ weeks              |  46.50 |  4.17 |  0.08 |      0 |
| 78+ weeks              |   8.58 |  0.42 |     0 |      0 |

_2026 averages cover January to July only._

The results show a substantial decline in long-waiting pathways after 2023, despite the continued growth in the overall incomplete waiting list. The average monthly number of pathways waiting 52 weeks or longer fell from approximately 156 in 2023 to 24 in January–July 2026. The average number waiting 65 weeks or longer also declined, reaching zero during the first seven months of 2026. No pathways waiting 78 weeks or longer were recorded from 2025 onwards.

This suggests that growth in the overall backlog has not been accompanied by a similar increase in the longest-waiting categories. One possible explanation is improved management of long-waiting cases. However, the available data cannot establish the reasons for this decline. Further analysis of incoming referrals and completed treatment pathways would be necessary to investigate whether changes in treatment activity contributed to the observed pattern.

The waiting-time categories are cumulative: pathways waiting 78 weeks or longer are also included in the 65+ and 52+ categories. Therefore, the figures should be interpreted as separate thresholds rather than added together.

### 4.6 Implications for Forecasting

The exploratory analysis identified several characteristics of the series that are relevant to forecasting:

- **Upward trend:** The backlog increased by 44.5% over the observation period. This raises the question of whether a forecasting model that assumes a constant future level can adequately represent the underlying movement.
- **Possible seasonality:** Incomplete pathways increased consecutively between May and July in each observed year. However, the 43-month series provides limited evidence for establishing a reliable annual seasonal pattern.
- **Unusual monthly movements:** The large decrease in March 2025 and increase in September 2025 warrant attention. Their causes are unknown, and they should not automatically be treated as data errors or removed from the analysis.
- **Changing waiting-time composition:** The number of pathways waiting 52 weeks or longer declined while the overall backlog increased. This demonstrates why total backlog volume alone does not fully describe waiting-list performance.
- **Limited historical observations:** The series contains 43 monthly observations. This limits the amount of historical information available for estimating trend and seasonality, making it important to compare more complex models against simple forecasting baselines.

These findings informed the subsequent model evaluation. In particular, the upward trend and possible recurring monthly patterns provided reasons to investigate ARIMA and SARIMA models alongside simpler baseline approaches. The final model selection was based on forecasting performance rather than the visual characteristics of the series alone.

## 5. Forecasting Methodology

This section describes how the forecasting models were developed and evaluated. The model comparison and forecast results are presented in Section 6.

### 5.1 Train-Test Split

The 43 monthly observations were split chronologically rather than randomly. This preserves the time order of the data, prevents future information from leaking into model training, and reflects how forecasts are used in practice.

- **Training set:** January 2023 to December 2025 (36 months).
- **Test set:** January to July 2026 (7 months).

Models were fitted using the training set and used to forecast the seven-month test period. The test observations were excluded from model fitting and used for the final holdout evaluation.

After model selection, the selected model was refitted using all 43 observations, from January 2023 to July 2026, to generate a six-month forecast covering August 2026 to January 2027.

### 5.2 Baseline Models

Four baseline models were included as benchmarks. More complex models were evaluated against these baselines to determine whether their additional complexity improved forecasting performance.

| Model            | Forecast rule                                                                                              |
| ---------------- | ---------------------------------------------------------------------------------------------------------- |
| Naive            | Repeats the most recently observed value.                                                                  |
| Historic Average | Uses the mean of all observations in the training data.                                                    |
| Seasonal Naive   | Repeats the observed value from the same month in the previous year, using a seasonal period of 12 months. |
| Window Average   | Uses the mean of the most recent three observations.                                                       |

The Naive model provides a useful benchmark because it carries the latest observed backlog level forward. This makes it particularly relevant when the series has an upward trend and recent observations may better reflect the current level than a long-term average.

The baseline models were evaluated using holdout Mean Absolute Error (MAE) and rolling-origin cross-validation.

### 5.3 ARIMA and SARIMA

ARIMA-based models were tested to assess whether modelling the time-series structure could improve on the baseline forecasts.

The models included:

- **ARIMA:** An automatically selected non-seasonal ARIMA model. The selected specification was ARIMA(0,1,0), without drift.
- **ARIMA with drift:** An ARIMA model with a drift term, allowing the forecast to incorporate an estimated average change over time.
- **SARIMA:** An automatically selected seasonal ARIMA model with a seasonal period of 12 months, to investigate whether incorporating an annual seasonal structure improved forecasting performance.

The non-seasonal ARIMA model selected by the automatic procedure was equivalent to the Naive model. An ARIMA(0,1,0) model without drift carries the latest observation forward, producing the same point forecasts as the Naive benchmark.

The seasonal model was included to test whether the recurring monthly movements observed during exploratory analysis provided useful predictive information. However, the training set contained only 36 observations, equivalent to three complete annual cycles. This limited the historical evidence available for estimating and evaluating annual seasonal patterns.

### 5.4 Time-Series Cross-Validation

Rolling-origin cross-validation was used as a second source of evidence alongside the holdout test. This approach evaluates models across multiple historical forecast periods rather than relying exclusively on one test period.

The cross-validation configuration was:

- **Number of windows:** 3
- **Forecast horizon per window:** 7 months
- **Step size:** 7 months
- **Window type:** Expanding
- **Data used:** Training set only (January 2023 to December 2025)
- **Refitting:** Models were refitted at each window.

At each iteration, the model was fitted using the available historical observations and used to forecast the next seven months. The training window then expanded before the next evaluation period.

The MAE scores were averaged across the three windows. This provided an additional comparison of model performance across historical periods. However, the evaluation remained limited by the short time series and the small number of validation windows.

### 5.5 Evaluation Metrics

Models were compared using Mean Absolute Error (MAE), which measures the average absolute difference between forecast and actual pathway counts.

MAE is expressed in the same unit as the target variable. For example, an MAE of 105.7 indicates that forecasts differed from the actual incomplete pathway counts by approximately 106 pathways on average.

MAE was used for both the holdout evaluation and cross-validation. Lower values indicate better forecasting accuracy. The same metric was retained across evaluations to make model comparisons consistent.

Prediction intervals were also generated for the final six-month forecast at the 80% and 95% levels. These intervals communicate the uncertainty surrounding the point forecasts by providing ranges within which future observations may fall.

The intervals should not be interpreted as guaranteed limits. Their usefulness depends on how well the model's assumptions and uncertainty estimates reflect the behaviour of future observations. Their historical performance was therefore also assessed using cross-validation.

## 6. Model Selection and Evaluation

This section compares the forecasting models using the seven-month holdout test and rolling-origin cross-validation. The objective was to identify a model that provides a reasonable balance between forecasting accuracy, simplicity and interpretability.

### 6.1 Holdout Test Results

Models were evaluated against actual incomplete pathway counts from January to July 2026 using Mean Absolute Error (MAE).

| Model                 | Holdout MAE |
| --------------------- | ----------: |
| Naive                 |      105.71 |
| ARIMA (without drift) |      105.71 |
| Window Average (3)    |      126.00 |
| ARIMA with drift      |      109.37 |
| SARIMA                |      283.31 |
| Seasonal Naive        |      532.00 |
| Historic Average      |      679.44 |

The Naive model achieved the lowest holdout MAE of approximately 105.71 pathways. ARIMA without drift produced the same result because its selected specification, ARIMA(0,1,0), is mathematically equivalent to the Naive forecasting method.

The Window Average and ARIMA with drift performed slightly worse, while SARIMA, Seasonal Naive and Historic Average produced substantially higher errors.

These results indicate that, among the models tested, carrying forward the latest observed backlog provided the most accurate forecasts for the January–July 2026 evaluation period.

### 6.2 Cross-Validation Results

Rolling-origin cross-validation provided an additional assessment across three historical forecast windows.

| Model              | Cross-validation MAE |
| ------------------ | -------------------: |
| SARIMA             |               150.11 |
| Naive              |               205.71 |
| Window Average (3) |               226.67 |
| ARIMA with drift   |               232.14 |

SARIMA achieved the lowest average cross-validation MAE, followed by Naive. This differs from the holdout results, where Naive performed best.

The difference suggests that model performance varied across evaluation periods. SARIMA performed better across the three historical validation windows but did not generalise as well to the January–July 2026 holdout period.

Cross-validation covered only three windows, each with a seven-month forecast horizon. The results should therefore be interpreted cautiously rather than treated as conclusive evidence of consistent seasonal behaviour.

### 6.3 Selected Model

The Naive model was selected for the final forecast based on its performance on the most recent holdout period, its simplicity and its interpretability.

Although SARIMA achieved a lower average cross-validation error, its holdout performance was considerably weaker. Given the limited historical observations and the absence of consistent evidence that the seasonal model would generalise to the most recent period, the Naive model was considered the more defensible choice for this forecast.

The selected model carries the July 2026 incomplete pathway count forward as the point forecast for each of the six forecast months. This is a baseline projection, not a claim that the backlog will necessarily remain unchanged.

The model selection reflects the evidence from the models and evaluation periods tested. It does not establish that the Naive model will outperform other approaches on future observations.

## 7. Final Forecast and Prediction Intervals

After selecting the Naive model, it was refitted using all 43 monthly observations, covering January 2023 to July 2026. A six-month forecast was generated for August 2026 to January 2027.

### 7.1 Six-Month Forecast

The Naive model carries forward the latest observed incomplete pathway count of 4,771.

| Forecast Month | Point Forecast |
| -------------- | -------------: |
| August 2026    |          4,771 |
| September 2026 |          4,771 |
| October 2026   |          4,771 |
| November 2026  |          4,771 |
| December 2026  |          4,771 |
| January 2027   |          4,771 |

The flat forecast follows directly from the Naive model's forecasting rule: each future observation is assigned the value of the most recently observed month. It should not be interpreted as evidence that the backlog has stabilised or that future pathway counts will remain unchanged.

### 7.2 Prediction Intervals

Prediction intervals communicate the uncertainty surrounding point forecasts by providing a range within which future observations may fall. Both 80% and 95% prediction intervals were generated for the six-month forecast.

| Forecast Month | Point Forecast | 80% Lower | 80% Upper | 95% Lower | 95% Upper |
| -------------- | -------------: | --------: | --------: | --------: | --------: |
| August 2026    |          4,771 |     4,593 |     4,949 |     4,499 |     5,043 |
| September 2026 |          4,771 |     4,520 |     5,023 |     4,386 |     5,156 |
| October 2026   |          4,771 |     4,463 |     5,079 |     4,300 |     5,242 |
| November 2026  |          4,771 |     4,415 |     5,127 |     4,227 |     5,315 |
| December 2026  |          4,771 |     4,373 |     5,169 |     4,163 |     5,379 |
| January 2027   |          4,771 |     4,335 |     5,207 |     4,105 |     5,437 |

The 95% intervals are wider than the 80% intervals because they represent a higher nominal coverage level. Both intervals widen with the forecast horizon, reflecting increasing uncertainty further into the future.

These intervals are not guaranteed minimum and maximum values. Their nominal coverage levels depend on the assumptions and uncertainty estimation method used to construct them.

### 7.3 Historical Assessment of Prediction Intervals

The prediction intervals were assessed using rolling-origin cross-validation to examine how often actual observations fell within the forecast ranges.

| Interval Level | Empirical Coverage | Average Interval Width |
| -------------- | -----------------: | ---------------------: |
| 80%            |             71.43% |                 587.38 |
| 95%            |             95.24% |                 898.32 |

The 80% intervals covered approximately 71.43% of the validation observations, while the 95% intervals covered approximately 95.24%.

The 95% intervals achieved empirical coverage close to their nominal level, whereas the 80% intervals fell below their nominal coverage. However, these estimates are based on only 21 validation observations across three windows. They should therefore be interpreted cautiously.

### 7.4 Forecast Interpretation

The forecast provides a baseline reference for monitoring the incomplete pathway backlog between August 2026 and January 2027.

The point forecast remains at 4,771 pathways, but the prediction intervals show that future observations may differ considerably from this estimate. For January 2027, the 95% interval extends from approximately 4,105 to 5,437 pathways.

The forecast should therefore be interpreted as a reference scenario rather than a definitive projection of future backlog levels. Actual monthly observations should be compared with the forecast and its intervals as new data become available.

## 8. Capacity-Planning Implications

The analysis provides several insights that may support elective care monitoring and capacity-planning discussions at Lancashire Teaching Hospitals NHS Foundation Trust.

### 8.1 Monitoring the Overall Backlog

Incomplete pathways increased from 3,301 in January 2023 to 4,771 in July 2026, representing a 44.5% increase over the observation period.

This sustained increase indicates growing backlog pressure within the selected Trauma and Orthopaedics treatment function. Regular monitoring of incomplete pathways can help identify whether the backlog is continuing to grow, stabilising or declining.

The forecast provides a six-month baseline against which subsequent monthly observations can be compared.

### 8.2 Identifying Periods of Increased Pressure

The exploratory analysis identified consecutive increases in incomplete pathways between May and July in each observed year.

This recurring pattern may justify closer monitoring during these months. However, the available observations are insufficient to establish a reliable annual seasonal effect or determine the operational causes of the increases.

Further investigation using referral and treatment activity data would be needed before translating this pattern into specific staffing or capacity decisions.

### 8.3 Monitoring Long-Waiting Patients

Although the overall backlog increased, the average monthly number of pathways waiting 52 weeks or longer declined substantially between 2023 and 2026.

This distinction is important for planning. The total backlog and the distribution of waiting times provide different information about service pressure. A growing backlog does not necessarily mean that the number of patients experiencing the longest waits is also increasing.

Planning teams should therefore monitor both total incomplete pathways and long-waiting pathway indicators.

### 8.4 Using Forecast Intervals as Monitoring References

The prediction intervals provide a range of possible future backlog levels rather than a single expected outcome.

Observed pathway counts approaching or exceeding the upper prediction bound could prompt further investigation into changes in referrals, completed activity and operational capacity. However, crossing an interval boundary does not automatically mean that additional capacity is required. It signals that actual performance differs from the model's expected range and may warrant review.

### 8.5 Connecting Backlog Forecasts to Operational Capacity

The forecast estimates future incomplete pathway counts; it does not directly calculate the number of additional appointments, procedures or staff required.

A more complete capacity-planning model would need to combine backlog information with:

- Incoming referrals and new RTT pathways.
- Completed admitted and non-admitted pathways.
- Treatment activity and throughput.
- Available clinical staff and theatre capacity.
- Waiting-time distributions and clinical prioritisation.

These additional indicators would help explain changes in the backlog and support more defensible estimates of the capacity required to manage it.

## 9. Limitations

Several limitations affect the interpretation and predictive reliability of this analysis.

### 9.1 Limited Historical Observations

The selected dataset contains 43 monthly observations covering January 2023 to July 2026. This is a relatively short time series for identifying long-term patterns and estimating annual seasonality.

Although recurring May–July increases were observed, three complete annual cycles provide limited evidence for establishing a consistent seasonal effect.

### 9.2 Single Provider and Treatment Function

The analysis focuses exclusively on Lancashire Teaching Hospitals NHS Foundation Trust (RXN) and Trauma and Orthopaedics (C_110).

The findings should not be generalised to other providers, treatment functions or the NHS as a whole without further analysis.

### 9.3 Backlog Data Does Not Explain Its Causes

The target variable measures incomplete RTT pathways at a point in time. It does not independently explain why the backlog increases or decreases.

Changes may be associated with incoming referrals, completed pathways, operational capacity or other factors, but these cannot be established using the selected dataset alone.

### 9.4 Model Limitations

The selected Naive model is simple and interpretable, but its point forecast carries the latest observed value forward without modelling the historical upward trend or possible seasonal patterns.

Its flat forecast may therefore fail to capture future changes in backlog levels.

The model was selected because it performed best on the most recent holdout period among the models tested. However, SARIMA performed better during cross-validation, demonstrating that model performance varied across evaluation periods.

### 9.5 Limited Evaluation Data

The holdout evaluation contains only seven observations, while cross-validation uses three windows with a seven-month forecast horizon.

These relatively small evaluation samples limit the strength of conclusions about how well the models will perform on future data.

### 9.6 Prediction Interval Uncertainty

Prediction intervals communicate uncertainty under the assumptions of the interval estimation method. Their historical coverage was assessed using only 21 cross-validation observations.

The observed coverage rates should not be treated as guarantees of future performance.

### 9.7 Exclusion of Operational Variables

The analysis does not incorporate referrals, treatment completions, staffing, theatre availability or other operational indicators.

Consequently, it cannot estimate the exact additional resources required to reduce the backlog or determine whether existing capacity is sufficient.

## 10. Monitoring and Future Improvements

The project provides a reproducible starting point for monitoring incomplete RTT pathways and evaluating baseline forecasting approaches. Several improvements could strengthen its usefulness for operational analysis.

### 10.1 Regular Data Updates

The data-processing workflow can be extended to incorporate newly published monthly NHS England RTT datasets.

Each update should validate the reporting period, provider and treatment function codes, missing values and duplicate observations before refreshing the consolidated dataset.

This would make it possible to compare actual monthly backlog counts against previous forecasts.

### 10.2 Forecast Performance Monitoring

Future observations should be compared with the model's point forecasts and prediction intervals.

Forecast errors should be tracked over time to determine whether the selected model continues to provide a useful baseline. If actual observations consistently depart from the forecast, the model should be reassessed.

### 10.3 Incorporating Referral and Treatment Activity

A significant improvement would be to combine incomplete pathway counts with monthly referral and completed pathway data.

This would provide a clearer picture of the factors contributing to backlog changes and help distinguish between increases associated with incoming activity and reductions associated with completed treatment.

### 10.4 Testing Additional Forecasting Approaches

As more observations become available, additional forecasting methods could be evaluated against the current Naive baseline.

Potential approaches include:

- Exponential smoothing methods.
- Alternative ARIMA and seasonal ARIMA specifications.
- Models incorporating external explanatory variables, where suitable data are available.

New models should only be adopted when they demonstrate improved performance on appropriate out-of-sample evaluations.

### 10.5 Interactive Monitoring Dashboard

An interactive dashboard could make the analysis more accessible to users who need to monitor backlog trends and forecast performance.

The dashboard could include:

- Historical incomplete pathway trends.
- Monthly changes in pathway counts.
- Waiting-time indicators and long-waiting pathway counts.
- Six-month forecasts with prediction intervals.
- Model evaluation results.
- Actual-versus-forecast comparisons as new data become available.

A dashboard would improve access to the analysis, but it would not replace the need for accurate data, appropriate forecasting methods or operational judgement.

## 11. Conclusion

This project developed a reproducible time-series forecasting workflow using NHS England Referral to Treatment data to examine incomplete pathways within the Trauma and Orthopaedics treatment function at Lancashire Teaching Hospitals NHS Foundation Trust.

The exploratory analysis identified a 44.5% increase in incomplete pathways between January 2023 and July 2026, alongside recurring mid-year increases and a substantial decline in the number of pathways waiting 52 weeks or longer. These findings demonstrate why overall backlog levels and waiting-time indicators should be considered together when monitoring elective care performance.

Several baseline and ARIMA-based forecasting models were evaluated using a chronological holdout test and rolling-origin cross-validation. The Naive model achieved the lowest MAE on the January–July 2026 holdout period and was selected for the final forecast, although SARIMA performed better across the historical cross-validation windows.

The selected model produced a six-month baseline forecast of 4,771 incomplete pathways per month from August 2026 to January 2027. Prediction intervals were included to communicate uncertainty rather than presenting the point forecast as a certain outcome.

The analysis demonstrates how historical healthcare data can be transformed into structured evidence for monitoring service pressure. However, forecasting the backlog alone cannot determine the resources required to manage it. Incorporating referral activity, completed pathways and operational capacity would be necessary to develop a more comprehensive capacity-planning approach.

Overall, the project provides a practical foundation for applying data science to healthcare performance monitoring and evidence-informed planning.
