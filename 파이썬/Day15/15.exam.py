
"""

< 객체지향 중요 개념 >

추상화: 객체로 정의할 대상에 대한 파악
        상속 시 공통 특성을 하나로 묶어 상위 타입을 정의

캡슐화: 관련 있는 속성과 행위를 하나로 묶어 정의(클래스)
        공개할 것과 은닉할 것을 분류(private, public, setter, getter 등)

상속: 기존 클래스를 확장하여 추가 특성을 정의( ~ is a ~ 고려)

다형성: 하나의 타입으로 다양한 타입을 다룰 수 있는 특성
        추상화와 상속의 개념을 활용하는 것

SOLID: 객체지향 설계원칙



< 정보 은닉 > 
파이썬에서 정보 은닉(외부 접근 제한)을 표현하는 방법
- _ (언더스코어) 문자를 이용하여 비슷한 개념을 표현(name mangling)

사용 방법
- _: 외부 접근을 제한한다는 개념 (타 언어에서의 protected 개념과 비슷, 강제성은 없음)
- __: 해당 형식에서만 접근 가능 (타 언어에서의 private 개념과 비슷, 강제성은 없음)


< setter, getter >
- setter: 객체에 속성을 설정하는 역할의 메서드
       = @x.setter (파이썬 데코레이터)
- getter: 객체의 속성을 반환하는 역할의 메서드
       = @property (파이썬 데코레이터)




"""











