# 2018-2-myMIMS

#[git 처음일 때 - 원격 저장소와 로컬저장소 연결]
1. git init
2. git remote add origin https://github.com/mingu9105/mims.git
3. git pull

#[git bash 사용할 때 - git bash, ubuntu linux 환경]
1. git add *
2. git commit -m "commit example"
3. git push origin master (-> branch 이름이 master인 원격 저장소로 push 한다, master 말고 본인 브랜치로 push를 하자.)

#[git source tree 처음일 때 - 원격 저장소와 로컬저장소 연결]
1. 깃 원격 저장소 복제
2. 저장소 - 깃플로우 - 저장소 초기화 - 확인
3. 브랜치 develop 체크된 것 확인
4. 저장소 - 깃플로우 - 새기능시작 - 이름 입력 - 확인
5. 브랜치 새기능이름 체크
6. 브랜치 새기능이름 오른쪽 클릭 - 가져오기 origin/develop (추적됨) - 가져오기 위한 원격 브랜치 develop 선택 - 확인

#[git source tree 원격 저장소에 push 하기]

#[개발환경]
0. windows10, x64 bit
1. python 3.6.5
3. VScode 1.30.1
4. Mysql 8.0.13
5. git 2.20.1

#[install library - pip install]
1. Django 2.1.3
2. pytz 2018.7
3. Pillow 5.3.0
4. mysqlclient 1.3.14
5. django_unixdatetimefield 0.1.6
6. requests 2.21.0

[install software]
1. git (https://git-scm.com/)
2. VScode (https://code.visualstudio.com/)
3. Mysql (https://dev.mysql.com/downloads/windows/installer/8.0.html)
4. sourcetree (https://www.sourcetreeapp.com/)

[process]
1. start project name myMIMS
2. add git flow (master, developer, feature) in sourcetree app
3. add django app name mapping
4. add image list page in mapping django app
5. add image detail page in mapping django app
6. connect image detail page and hyperledger fabric
7. change database sqlite3 to mysql

[오류해결]
