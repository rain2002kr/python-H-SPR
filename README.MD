# 목적 : 오더 트래킹 관리와 커스터머 리퀘스트데이트를 관리하는데 목적이있다.

---

## DESKTOP 동작확인 완료 버전

## 작업 완성 목표 .

    * 기능 0 : 화면 이동
        * SPR 등록 화면
        * SPR 검색 화면

    * 기능 1 : 초기화
        * FILE READ 엑셀 만들기
        * SPR SUM 엑셀 만들기

    * 기능 2 : 스크린 지우기
        * 스크린1 화면 지우기

    * 기능 3 : LOAD 서버
        * SPR 번호가 없다면, SUM_SPR 테이블 전체를 읽어온다.

    * 기능 4 : SAVE 서버
        * SPR SUM 엑셀내용을 서버에 저장한다.

    * 기능 5 : SPR SUM 읽어오기
        * SPR SUM 엑셀파일을 읽어와서 VIEW 테이블에 뿌려준다.

    * 기능 6 : LOAD SPR 엑셀
        * SPR 번호검색창에 있는 정제된 SPR 엑셀을 그대로 읽어와서 뿌려준다.

    * 기능 7 : SAVE 엑셀
        * 지정된 SPR 번호를 전체 SPR 에 저장한다.

    * 기능 8 : 폴더내 엑셀 LOAD
        * SPR 번호검색창에 있는 SPR 엑셀을 그대로 읽어와서 뿌려준다.

    * 기능 9 : SAVE 전체 엑셀
        * 폴더안에 있는 SPR

    * 기능 10 : LOAD SPR INFO 1
        * SPR INFO 엑셀 시트1 불러오기

    * 기능 10 : LOAD SPR FILE JOB1
        * 작업 완료파일과 완료전파일 읽어와서 비교하기

    * 기능 11 : LOAD SPR FILE JOB2-TEMP
        * SPR FILE 내용 불러와서 뿌려주기

    * 기능 12 : CONVERT
        * SPR 번호검색창내용 가지고, SPR RAW 안에 있는 내용 저장하기

    * 기능 13 : CONVERT ALL
        * SPR RAW 안에 있는 모든 엑셀 파일을 저장하기

    * 기능 14 : 프로그래스바
        * 각 작업 프로세스 DONE 에 대해 표기한다.
