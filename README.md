# programmers
### programmers 알고리즘 풀이
-----------------
## 1회차 1_class
**문제 별 해결방법**

- 1.평균 구하기 : 성공
    - 해경방법 : 배열의 합(sum) / 배열의 길이(len)

- 2.짝수와 홀수 : 성공
    - 해결방법 : 2로 나눴을때 나머지 0과1에 따라 나눔 

- 3.자릿수 더하기 : 성공
    - 정수 n을 자릿수별로 나누기 위해 str()로 나눈뒤 다시 int로 바꿔준 뒤 합을 구함

- 4.자연수 뒤집어 배열로 만들기 : 성공
    - 해결방법 일단 주어진 자연수를 끝에서 불러올 수 있게 문자열로 바꿔준뒤 문자열의 맨뒤에서부터 for문을 반복해 한자리씩 가져온 뒤 정수로 다시 바꿔주고 배열에 append 해준다. 

- 5.숫자 문자열과 영단어 - 2021 카카오 채용연계형 인턴십 : 성공 !
    - 해결방법 : replace로 바꿔준 숫자는 str 형식으로 숫자가 아닌 문자로 인식하기때문에 마지막에 int로 묶어줘서 숫자로 인식 할 수 있게 해줬다.

- 6.체육복 - 탐욕법(Greedy) : 실패 !!
    - 어떠한 방식으로 풀면 되겠다라는 감만 잡히고있다..

- 7.비밀지도 - 2018 KAKAO BLIND RECRUITMENT : 실패 !!
    - and, or 비트연산 문제인건 알겠지만 해당 연산을 어떻게 코드로 진행시켜 나아가야 할지 모르겠음..

- 8.약수의개수와덧셈-월간코드챌린지시즌2 : 성공 !
    - 해결방법 : 약수의 갯수는 1부터 자기자신까지 나눠서 나머지가 0이면 해당 숫자의 약수이다. 그래서 나머지가 0이면 count에 1씩 더해줬고, 해당 숫자의 약수를 모두 구했으면 count가 짝수인지 홀수인지 나눠서 "+ / -" 부호를 붙여준뒤 모두 더해줬다.

- 9.없는숫자더하기-월간코드챌린지시즌3 : 성공 !
    - if 문의 not in 구문을 활용해 해결

- 10.완주하지 못한 선수 – 해시 : 실패 !!
    - 정확성 테스트는 통과 했으나 효율성 테스트에서 시간 초과로 실패


-----------------
## 2회차 2_class
**문제 별 해결방법**

- 1.두 정수 사이의 합 : 성공
    - 해경방법 : 대소관계가 주어지지 않기 때문에 if문으로 대소관계를 정의해준뒤 합을 구함

- 2.문자열을 정수로 바꾸기 : 성공
    - 해결방법 : 주어진 문자를 int()에 넣어 변환 후 반환

- 3.정수 내림차순으로 배치하기 : 성공
    - 해결방법 : join함수를 이용하여 해결

- 4.나머지가1이되는수찾기-월간코드챌린지시즌3 : 성공
    - 해결방법 : for문이 아니라 while문을 사용해 내가 원하는 조건을 만족 했을때 break!

- 5.음양더하기-월간코드챌린지시즌2 : 성공
    - 해결방법 : 주어지는 배열의 길이가 같다는걸 이용해 정의해주었다.

- 6.예산 - Summer/Winter Coding(~2018) : 성공
    - 해결방법 : 배열 d에서 제일 작은부서부터 챙겨주면 최대한 많은 부서를 챙겨줄 수 있고, d에서 원한 예산이 budget보다 작거나 같으면 계속해서 지원이 가능하다. 

- 7.K번째수 - 정렬 : 성공
    - 해결방법 : 2차원 배열 개념이 있어야됨 + 배열의 시작은 0부터 이다.

- 8.같은숫자는싫어-스택/큐 : 성공
    - 해결방법 : stack 이라는 배열의 맨 끝과 지금 내가 append할 수가 같지 않으면 stack에 넣어줘, 근데 맨 처음 stack안 아무 원소도 없을땐 stack[-1]이 오류가 나서 stack에 들어갈 수 없는 10이라는 수를 임의로 넣어준 후 모든 연산이 끝난 후 빼줬다.

- 9.실패율 - 2019 KAKAO BLIND RECRUITMENT : 성공
    - 해결방법 : 딕셔너리를 활용해서 해결 자세한 풀이는 문제에!

- 10.소수 만들기 - Summer/Winter Coding(~2018) : 성공
    - 해결방법 : 튜터님 Tip! 자세한 풀이는 문제에!


-----------------
## 3회차 3_class
**문제 별 해결방법**

- 1.문자열내p와y의개수 : 성공
    - 해결방법 : 배열을 for 문으로 하나씩 가져오기

- 2.핸드폰 번호 가리기 : 성공
    - 해결방법 : replace 함수와 len 함수 활용

- 3.제일작은수제거하기 : 성공
    - 해결방법 : min()함수와, remove를 이용해 해결

- 4.콜라츠 추측 : 성공
    - 해결방법 : num == 1에 대한 조건을 맨 처음에 배치해준뒤 while문 돌리기

- 5.수박수박수박수박수박수? : 성공
    - 해결방법 : 문자열도 연산 가능

- 6.가운데 글자 가져오기 : 성공
    - 해결방법 : len함수의 활용

- 7.올바른 괄호 - 스택/큐
    - 해결방법 :
