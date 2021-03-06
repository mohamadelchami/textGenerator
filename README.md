# Automated Social Media Spear-Phisher 

created as part of a overall Fb-Twitter-gui repository. Please refer to that repo. 

## Authors: 
- Abdullah Arif
- Abdullah Chattha
- Ashraf Taifour
- Mohamad Elchami
- Steve Pham

## Supervisor
  Dr. Sherif Saad Ahmed

## Adding packages
`pip3 install -r requirements.txt`
 
## How to run
  The program execution is reliant on the output of the Facebook Scrapper. That being said make sure to have the path to the scraped files passed into the program when calling it or that they are located in the same directory as textGenerator.py upon execution.
  `python3 phishingTextGenerator.textGenerator.py`

# What is this? 🤔
Phishing attacks accounted for 80% of security incidents [[2](https://www.csoonline.com/article/3153707/top-cybersecurity-facts-figures-and-statistics.html)]. And the pandemic has increased the number of cyber attacks[[5](https://www.who.int/news-room/detail/23-04-2020-who-reports-fivefold-increase-in-cyber-attacks-urges-vigilance)]. So, it is imperative that we study different social attacks. There is a more potent type of phishing called “spear-phishing”, where an attacker gathers information about a user and uses that to craft a more persuasive message. This technique has a much higher click through rate than average phishing attacks. Fortunately, this method is time-consuming and so the attacker cannot target as many people. However, we believe that you can use machine learning to automate this process. If this process becomes widespread, it would have disastrous consequences.

Our project will be to create this automated spear-phishing tool. We will then use our tool to analyze them to determine the effectiveness of various algorithms and the vulnerability on different platforms. We also hope to show the potency of this attack. So, we will compare it to normal phishing attacks and compare the results. We hope the results from our study will help future developers and cybersecurity researchers to create more effective safeguards against social attacks.

Most malware comes from email. However, there is a rising trend for phishing attacks conducted on social media. This is because social media contains a plethora of personal information which makes it possible to launch this type of automated spear-phishing attack.

Rather than creating a defensive tool like a phishing detector using machine learning, we have created an offensive tool. This is because when people are trying to break things, they look for the easiest ways to get the job done. The principle of easiest penetration states that a security system is as strong as its weakest link. So by thinking like an attacker, we can become better defenders.\
[1]: https://www.fundera.com/resources/small-business-cyber-security-statistics \
[2]: https://www.csoonline.com/article/3153707/top-cybersecurity-facts-figures-and-statistics.html \
[3]: https://enterprise.verizon.com/resources/reports/dbir/2020/results-and-analysis/ \
[4]: https://www.phishingbox.com/news/phishing-news/internet-security-threat-report-irst-2019. \
[5]: https://www.who.int/news-room/detail/23-04-2020-who-reports-fivefold-increase-in-cyber-attacks-urges-vigilance 
