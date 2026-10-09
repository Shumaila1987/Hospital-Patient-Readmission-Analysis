# Hospital-Patient-Readmission-Analysis
 
This project started with a simple question: can we spot patterns in hospital data that help us understand why some patients return sooner than others?
 
I worked with a real dataset from 130 US hospitals, covering diabetes patient records over 10 years. It wasn't clean data — that's the first thing I noticed. Some columns were mostly empty, some values were marked with question marks instead of being clearly recorded, and a few records didn't have complete information. So I began by cleaning it properly in Python — removing what I couldn't use, standardising what I could, and saving a fresh, reliable version of the data to work with.
 
From there I explored the numbers. What stood out most was that just over half of patients didn't come back at all — that's encouraging. But about 11% were readmitted within 30 days. Those patients tended to have stayed a little longer during their first visit, and were managing more medications on average. I also looked at how this changed across different age groups — older patients showed different patterns than younger ones, which makes sense but is worth seeing clearly.
 
Then I built a dashboard in Power BI so anyone can see these patterns at a glance. It shows the total number of patients, average stay length, average medications, the breakdown of readmission rates, and how readmission changes by age group.
 
This project taught me that good analysis isn't just about running code or making charts. It's about understanding what the data represents, being honest about its limitations, and finding insights that are actually useful. If hospitals can identify patients who might need a little extra support after discharge — someone staying longer or taking more medicines — they can step in before readmission becomes necessary. That's the real value in work like this.
  
What I Used
 
- Python & Pandas — data cleaning and analysis
​
- Power BI — interactive dashboard and visualisation
​
- Source data: Available on Kaggle — search "Diabetes 130-US Hospitals for years 1999–2008"
 
My cleaned version:  data/diabetic_data_cleaned.csv  (included in this repo)
 
Project Files
 
-  healthcare_analysis.py  — full Python code
​
-  data/diabetic_data_cleaned.csv  — cleaned dataset
​
-  dashboard_screenshot.png  — dashboard preview
​
-  dashboard_demo.mp4  — short video walkthrough
 
 
Shumaila Liaqat
