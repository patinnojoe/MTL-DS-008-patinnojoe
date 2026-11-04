1. Figure One - Incomplete Pathways per Month

   The Line plot shows the trend for montly incomplete pathways for _Lancashire Teaching Hospital (LTH), Trauma and Orthopaedic Service (TOS) from 2023 January to 2026 July_.
   The general trend direction suggests an upward trend. The starting period recorded _3301_ monthly incomplete RTT while the closing date recorded _4771_ of incomplete RTT , which is a _44.5%_ increase. This suggests that there is a significant demand and pressure in LTH for TOS within the observed period.
   Throughout the observed periods, there was an observed fluctuation month to month, however the period between May and July across each year, had an identified pattern. between May and July the number of incomplete pathways generally increases.
   For context, _May 2023 - 3268_, _June 2023 - 3465_, _July 2023 - 3679_ , _May 2024 - 3534_, _June 2024 - 3601_, _July 2024 - 3725_ and this pattern is same for _May 2025 - 3908_, _June 2025 - 4032_, _July 2025 - 4084_ and lastly for 2026 _May - 4447_, _June - 4561_, _July - 4771_
   So for the period between May and July each previous month has an increased number of RTT than the preceeding month, this may imply a pressure point each year, although the gragh can not completely explain that.

2. Figure Two - Month by Month Percentage Change of RTT

   The graph shows fluctuations, with some changes positive and some negative, however, positive changes appeared more frequent in the chart, indicating an upward trend of incomplete pathways over time.
   From the period understudy, the year _2025_ holds both the largest and smallest percentage changes.
   _March 2025_ recorded a percentage change of _-6%_ making it the month with the lowest change rate, as incomplete pathways fell from the Feburary 2025 _4114_ figure to _3867_ in _March 2025_ .
   _September 2025_ holds the largest percentage difference with a _9.77_ change rate, the number of incomplete pathways increased from _4060_ the previous month to _4457_ in _September 2025_.

3. Figure Three - Seasonality Trend

   The trend shows generally that incomplete pathways are increasing. 2023, which is the begining year under review has the lowest overall total number of inconplete pathways, 2024 has a general higher total number of incomplete pathway than 2023, same overall increase is observed as 2026 has higher overal total number of incomplete pathways than 2025.

4. Figure Four - Average (Median) Waiting time

   The observation from the Average median waiting time indicates an overall increase in the average waiting time year on yearhowever, each year, the direction of the average waiting time median is declining. the highest recorded decline is in 2025, where the average median collasped from a value of 15.9 weeks in sepetember of 2025 to 10.7 weeks in November.A worthy observation is that, the average median time generally declines from march to June, from 2023-2025, however, 2026 average waiting time within this period goes the opposite direction another important observation is that the average waiting time generally picks up in November of every year, as the year 2023-2025 shows that at this time patients would most likely wait the longest.

5. Figure Six – Long-Waiting RTT Pathways (52+, 65+ and 78+ Weeks)

   The bar chart compares the average monthly number of incomplete RTT pathways waiting 52 weeks or longer, 65 weeks or longer, and 78 weeks or longer between 2023 and 2026.

   Interestingly, the results show a general decline in long-waiting pathways after 2023, despite the overall incomplete waiting list increasing during the same period.

   In 2023, the hospital recorded an average of 156.25 pathways waiting 52 weeks or longer, compared with 52.58 in 2024, 36.25 in 2025 and 24.14 in 2026. A similar decline is observed among patients waiting 65 weeks or longer, which fell from an average of 46.50 in 2023 to zero in 2026. The number of pathways waiting 78 weeks or longer also declined from 8.58 in 2023 to zero from 2025 onwards.

   This suggests that although the overall waiting list continued to grow, the number of patients experiencing very long waits reduced substantially after 2023. One possible explanation is that the hospital may have improved its handling of long-waiting cases, while the continued increase in incomplete pathways may indicate growing pressure on its overall waiting-list capacity.

   However, the available data cannot establish the reasons behind these changes. Further investigation into referral rates and treatment completion would be necessary to understand whether improvements in handling long-waiting cases occurred alongside increasing demand.

6. model selection and evaluation

   Model selection and evaluation
   The baseline models were developed and evaluated using Mean Absolute Error (MAE). Among the baseline forecasting strategies, the Naive model achieved the lowest MAE, indicating that it produced the most accurate forecasts among the baseline models tested.

   To investigate whether more advanced time-series models could improve forecasting accuracy, ARIMA and SARIMA models were subsequently evaluated. The ARIMA model achieved an identical MAE to the Naive model, suggesting that it did not provide a measurable improvement over the baseline approach. The SARIMA model performed worse on the test dataset.

   These results suggest that the additional complexity of the ARIMA and SARIMA models did not translate into improved forecasting accuracy for the observation period considered. Therefore, the Naive model remains a strong candidate for the final forecasting model, subject to further validation using rolling-origin cross-validation.
