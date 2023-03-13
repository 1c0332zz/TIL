package hello.hellospring.controller;


import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.ResponseBody;

// 컨트롤러는 어노테이션을 꼭 해줘야함
@Controller
public class HelloController {
    @GetMapping("hello") // HTTP 의 GET
    public String hello(Model model) {
        model.addAttribute("data", "Spring!!"); // Key = 데이터, Value = 값
        return "hello"; // templates 의 하위 폴더에 hello.html 을 찾아감
    }

    @GetMapping("hello-mvc")
    public String helloMvc(@RequestParam("name") String name, Model model) { // 이대로 넘길려면 ?name=~~~
        model.addAttribute("name", name); // 파라미터에서 넘겨온 네임을 넘겨줌
        return "hello-template";
    }

    @GetMapping("hello-string")
    @ResponseBody // http 의 body 부분에 이 데이터를 직접 넣어주겠다. => 이 데이터를 그대로 화면에 보여줌 => 문자일 경우
    public String helloString(@RequestParam("name") String name) {
        return "hello " + name; // hello spring(name)
    }

    // 데이터를 내놓는 진짜 API 방식
    @GetMapping("hello-api")
    @ResponseBody
    public Hello helloApi(@RequestParam("name") String name) {
        // 객체일 경우
        Hello hello = new Hello();
        hello.setName(name);
        return hello; // return: hello(name:spring)
    }

    static class Hello {
        private String name; // private 이라 외부에서 못꺼냄

        // Java Bin 표준 방식 => Getter&Setter
        public String getName() { // 꺼낼떄는 get
            return name;
        }

        public void setName(String name) { // 넣을때는 set
            this.name = name;
        }
    }
}
