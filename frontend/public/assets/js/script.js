import ReactDOM from 'react-dom';

$(document).ready(function() {


    /**
     * 라이브러리 스크립트.
     */
    project.init();

    
});

var project = {
    init : function () {
        project.gnbMove();
        project.maxHeight();
    },
    maxHeight : function(){
        /**
         * 서비스 박스 높이값맞추기
         */
        var max_h = 0;
        $(".box .step p").each(function () {
            var h = parseInt($(this).css("height"));
            if (max_h < h) {
                max_h = h;
            }
        });
        $(".box .step p").each(function () {
            $(this).css({
                height: max_h
            });
        });
    },
    gnbMove : function(){
        //클릭시 이동
        $('.gnb ul li > a').click(function(){

            var id = $(this).attr("href");

            var y = $(id).offset().top;

            $("html, body").stop().animate({scrollTop:y - 100}, 500);

        });

        $('.logo').on('click' , function(){
            $('html').animate({scrollTop: 0} , 300);
        })
    }
};


ReactDOM.render(<App />, document.getElementById('root'));

