# Chuck Chau Resume on github
In the past, I maintained my resume using MS Word then Google Doc, and end up with multiple versions of resumes all over hard drives, cloud drives and email attachments.  However, as a software developer, I believe resume should be written in machine understandable format and stored in source control for change tracking.  In general, 2 pages resume is the street standard, but that may not have enough space to hold all details that are related to prior experiences.  2+ pages resume help readers to form a better picture of previous works and ask questions in interview, but not everyone have patient to read it through.

## Solution
I store my experiences data in detail with yaml files, and then generate different versions of html resume, using python templating with pystache.  The pdf copy is exported from html version.

## Resumes
+ [Standard 2 pages Resume (html)](http://htmlpreview.github.io/?https://github.com/volkstrader/resume/blob/master/python/resume.html)
+ [Standard 2 pages Resume (pdf)](https://github.com/volkstrader/resume/blob/master/Chuck%20Chau%20Resume%20Standard.pdf)
+ [Standard 2 pages Resume (docx)](https://github.com/volkstrader/resume/blob/master/Chuck%20Chau%20Resume%20Standard.docx)

## Usage
### Generate html
    cd python
    python gen-resume.py > resume.html
    
### Serve html locally
    python3 -m http.server
