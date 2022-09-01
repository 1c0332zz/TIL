### justify-content : Flex요소를 가로선 상에서 정렬한다.
* flex-start: 요소들을 컨테이너의 왼쪽으로 정렬합니다.
* flex-end: 요소들을 컨테이너의 오른쪽으로 정렬합니다.
* center: 요소들을 컨테이너의 가운데로 정렬합니다.
* space-between: 요소들 사이에 동일한 간격을 둡니다.
* space-around: 요소들 주위에 동일한 간격을 둡니다.

### align-items : Flex요소를 세로선 상에서 정렬한다.
* flex-start: 요소들을 컨테이너의 꼭대기로 정렬합니다.
* flex-end: 요소들을 컨테이너의 바닥으로 정렬합니다.
* center: 요소들을 컨테이너의 세로선 상의 가운데로 정렬합니다.
* baseline: 요소들을 컨테이너의 시작 위치에 정렬합니다.
* stretch: 요소들을 컨테이너에 맞도록 늘립니다.

### flex-direction : 정렬할 방향을 지정한다.
* row: 요소들을 텍스트의 방향과 동일하게 정렬합니다.
* row-reverse: 요소들을 텍스트의 반대 방향으로 정렬합니다.
* column: 요소들을 위에서 아래로 정렬합니다.
* column-reverse: 요소들을 아래에서 위로 정렬합니다.

### order : Flex요소의 순서를 지정한다.
* <integer> (... -1, 0 (default), 1, ...)
* order : 1;

### align-self : 지정된 `align-items` 값을 무시하고 Flex요소를 세로선 상에서 정렬한다.
* flex-start: 요소들을 컨테이너의 꼭대기로 정렬합니다.
* flex-end: 요소들을 컨테이너의 바닥으로 정렬합니다.
* center: 요소들을 컨테이너의 세로선 상의 가운데로 정렬합니다.
* baseline: 요소들을 컨테이너의 시작 위치에 정렬합니다.
* stretch: 요소들을 컨테이너에 맞도록 늘립니다.

### flex-wrap : flex요소들을 한 줄 또는 여러 줄에 걸쳐 정렬한다.
* nowrap: 모든 요소들을 한 줄에 정렬합니다.
* wrap: 요소들을 여러 줄에 걸쳐 정렬합니다.
* wrap-reverse: 요소들을 여러 줄에 걸쳐 반대로 정렬합니다.

### align-content : 세로선 상에 여분의 공간이 있는 경우 Flex 컨테이너 사이의 간격을 조절합니다.
align-content는 여러 줄들 사이의 간격을 지정하며, align-items는 컨테이너 안에서 어떻게 모든 요소들이 정렬하는지를 지정합니다. 한 줄만 있는 경우, align-content는 효과를 보이지 않습니다.
* flex-start: 여러 줄들을 컨테이너의 꼭대기에 정렬합니다.
* flex-end: 여러 줄들을 컨테이너의 바닥에 정렬합니다.
* center: 여러 줄들을 세로선 상의 가운데에 정렬합니다.
* space-between: 여러 줄들 사이에 동일한 간격을 둡니다.
* space-around: 여러 줄들 주위에 동일한 간격을 둡니다.
* stretch: 여러 줄들을 컨테이너에 맞도록 늘립니다.

### flex-flow : flex-direction 과 flex-wrap의 합