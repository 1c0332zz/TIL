## Json

1. 사용자 생성 데이터로부터 JSON객체 생성
2. 시스템 간 데이터 전송
3. 애플리케이션용 데이터 구성
4. 복잡한 데이터 모델 간소화

* 데이터를 관계형(구조적) 형식이 아닌 문서 모델 형식(반 구조적)으로 저장

```json
{
  "이름공간(키)": "값",
  "값 구분자": "각각의 값들은 ',' (콤마)로 구분되어야 합니다.",
  "이스케이프": "키나 값에서 큰따옴표를 쓰고 싶으면-특정 문자를 이스케이프 하려면- \" 처럼 문자 앞에 역슬래시를 붙입니다.",
  "자료형": "표현 가능한 자료형은 문자열, 숫자, 불리언, 널, 객체, 배열 6개입니다.",
  "문자열 값": "나무위키, 여러분이 가꾸어 나가는 지식의 나무",
  "숫자 값": 19721121,
  "불리언 값": true,
  "널 값": null,
  "객체 값": {
    "값1": 3.141592653589793,
    "값2": false,
    "값3": {
      "객체 안에": "객체를 넣는것도 가능하지요",
      "구분자": "또한 키와 값은 ':' 로 구분됩니다"
    }
  },
  "배열 값": [
    "이것은 배열입니다.",
    {
      "현재 값의 인덱스": 1,
      "이런 식으로": "배열 안에 여러 값을 넣을 수 있습니다."
    },
    [ "배열", "안에", "배열을", "넣는것도", "가능하지요" ]
  ],
  "값의 개수가 적을때는": "다음과 같이 한 줄로도 객체와 배열 표현이 가능합니다.",
  "한 줄 객체": { "김두한": "개소리 집어쳐", "심영": "내가 고자라니", "의사양반": "전화는 없어요" },
  "한 줄 배열": [ "나무위키는", "누구나", "기여할", "수", "있는", "위키입니다." ]
}
```

> 파이썬에선 본인만의 객체 세계에 맞춰서 변환해서 사용
>
> js에선 배열안에 객체로 해석

* 이 변환하는걸 (해석) 파싱(인코딩)이라고 한다. 
  * 이를 파이썬에선 리스트안에 딕셔너리로 해석 (parsing)
  * js에선 배열안에 객체로 해석 (parsing)

### epoch time

* 시간은 에포크 타임