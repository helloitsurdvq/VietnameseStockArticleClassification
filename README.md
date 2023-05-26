# Intro to AI (IT3160E) Capstone Project - Group 07

## Corporate Stock Review 

### Overview
In this project, we will implement sentiment analysis techniques to analyze stock reviews to
evaluate how the sentiment impacts stock performance. Positive reviews can drive up the stock
price and attract more investors, while negative reviews can cause a decline in stock price and
investor confidence. The aims of this project is to implement a sentiment classifier to:
- Assign a large set of corporate stock reviews to the several levels of polarity of opinion as
accurately as possible.
- Identify the most commonly mentioned positive and negative aspects of the organization

Here is the output model that we have trained (including phoBERT, DBLSTM, DBGRU): [Link drive](https://drive.google.com/drive/folders/1fV3k4jnYKowYhtSTEi60p7Uek5oM_lGk?usp=sharing)

### Project Organization
```
app/                        # model deployment
crawler/                    # data collection program (using Scrapy)
data/                       # raw and processed data collected from websites
idea/                       # initial proposed idea for project
source                      # processed data and jupyter notebooks for the pipeline
-- ./data/                  # processed data
-- .ipynb                   # all trained models from modelling
report                      # project report and presentation
.gitignore
README.md        
```
### Data Source
Vietnamese major articles on business and finance (CafeF, VnExpress etc.)

### Contributing 🔧
If you want to contribute to this project and make it better with new ideas, your pull request is very welcomed.
If you find any issue just put it in the repository issue section, thank you.

### Collaborators
<table>
    <tbody>
        <tr>
            <th align="center">Member name</th>
            <th align="center">Student ID</th>
        </tr>
        <tr>
            <td>Nguyễn Chí Long</td>
            <td align="center"> 20210553&nbsp;&nbsp;&nbsp;</td>
        </tr>
        <tr>
            <td>Ngô Xuân Bách</td>
            <td align="center"> 20215181&nbsp;&nbsp;&nbsp;</td>
        </tr>
        <tr>
            <td>Lê Xuân Hiếu</td>
            <td align="center"> 20215201&nbsp;&nbsp;&nbsp;</td>
        </tr>
        <tr>
            <td>Đinh Việt Quang</td>
            <td align="center"> 20215235&nbsp;&nbsp;&nbsp;</td>
        </tr>
    </tbody>
</table>
