from jira import JIRA
import re

try: 
	options = {'server': 'http://localhost:9090'}
	jira = JIRA(options,basic_auth=('Muralikrishna','Murali@789'))
	summary = "Vulnerability Descriptions"
	with open('Assessment.xml','r') as myfile:
		data = myfile.read()
	issue_dict = { 'project' : {'key':'TEST'}, 'summary' : summary , 'description' : data ,'issuetype' : {'name':'Task'}}
	new_issue = jira.create_issue(fields=issue_dict,preftech=True)
	print new_issue
except Exception,e:
	print str(e)
