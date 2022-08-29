# CSS: cascading Style Sheets

**Cascading Style Sheets**(**CSS**)는 [HTML](https://developer.mozilla.org/ko/docs/Web/HTML)이나 [XML](https://developer.mozilla.org/ko/docs/Web/XML)(XML의 방언인 [SVG](https://developer.mozilla.org/ko/docs/Web/SVG), [XHTML](https://developer.mozilla.org/ko/docs/Glossary/XHTML) 포함)로 작성된 문서의 표시 방법을 기술하기 위한 [스타일 시트](https://developer.mozilla.org/ko/docs/Web/API/StyleSheet) 언어입니다. CSS는 요소가 화면, 종이, 음성이나 다른 매체 상에 어떻게 렌더링되어야 하는지 지정합니다.

## 그래서 CSS가 무엇인가?

* *Style sheet 언어*
* HTML 문서에 있는 요소들에 **선택적으로 스타일을 적용**
* 예를 들면, HTML 페이지에서 **모든** 문단 요소들을 선택하고 그 문단 요소들 안에 있는 텍스트를 빨갛게 바꾸려고 한다면 다음과 같이 CSS를 작성할 것입니다.

```css
p {
  color: red;
}
```

### CSS의 ruleset

