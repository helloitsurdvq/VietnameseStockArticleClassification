# Intro to AI (IT3160E) Capstone Project - Group 07

## Corporate Stock Review 

### Overview
In this project, we will implement sentiment analysis techniques to analyze stock reviews to
evaluate how the sentiment impacts stock performance. Positive reviews can drive up the stock
price and attract more investors, while negative reviews can cause a decline in stock price and
investor confidence. The aims of this project is to implement a sentiment classifier to:
- Assign a large set of corporate stock reviews to the several levels of polarity of opinion as
accurately as possible.
- Identify the most commonly mentioned positive and negative aspects of the organization.


### Project Organization
```
app/                        # model deployment
crawler/                    # data collection program (using Scrapy)
data/                       # raw and processed data collected from websites
docs/                       # project report and presentation
source/                     # processed data and jupyter notebooks for the pipeline
-- ./data/                  # processed data
-- .ipynb                   # all trained models for evaluation
.gitignore
README.md        
```
### Data Source
Vietnamese major articles on business and finance (CafeF, VnExpress etc.).

### Setup
*We highly recommend you to use the google colab (pro) version because of its built-in libraries and our models are quite large (~500mb)*
- Setup environment for local machine:
```
python -m venv venv
cd venv\Scripts
.\activate
```
- Please download all necessary library for these following works.
- For evaluation, run each notebook file in `source` folder.
- For testing, to run this project, you first have to download all mentioned weights files of model. Then simply run each notebook of our project in `source/07_demo.ipynb` file
- To run the web application, please run the notebook file `deployment_ColabVersion.ipynb` or run directly on local from `app/app.py`.

Here is the weights file of trained models: [Drive Link](https://drive.google.com/drive/folders/1fV3k4jnYKowYhtSTEi60p7Uek5oM_lGk?usp=sharing).

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