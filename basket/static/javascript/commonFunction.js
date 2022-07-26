var scrollBarWidth = 0;
$(function() {
    scrollBarWidth = getScrollBarWidth();
    //상단 검색
    var $srcOpenBtn = $('.layerOpen'),
        $srcCloseBtn = $('.layerClose'),
        $srcArea = $('.siteSearchWrap');

    $srcOpenBtn.on('click',function(){
        $(this).addClass('active');
        $srcArea.slideDown(200);
        $('body').addClass('blackWrap');
    });

    $srcCloseBtn.on('click',function(){
        $srcOpenBtn.removeClass('active');
        $srcArea.slideUp(200);
        $('body').removeClass('blackWrap');
    });

    var $body = $('body'),
        scrollFixedTop = function() {
            if($(this).scrollTop() > 0){
                $body.addClass('fixedTop');
            } else if($(this).scrollTop() <= 0 && $body.hasClass('fixedTop')){
                $body.removeClass('fixedTop');
            }
        };
    scrollFixedTop();
    $(window).scroll(function(){
        scrollFixedTop();
    });
});

/**
 * 탭 컨텐츠
 * @param object
 */
function tabContent (tabCntWrap, tabButton, tabCnt) {

    var $tabWrap = $(tabCntWrap),
        $tabButton = $tabWrap.find(tabButton),
        $tabContent = $(tabCnt);

    $tabButton.on("click", function(){

        var $currentTarget = $(event.currentTarget);

        $tabWrap.find(".active").removeClass("active");
        $tabWrap.find($tabContent).css({"display":"none"});
        $currentTarget.addClass("active");
        $currentTarget.next($tabContent).addClass("active").css({"display":"block"});

    });
}

//spy scroll
function spyButton(spyWrap, breakPoint, defaultPosition, bottomPosition){
    var ScrollEvent = function() {
        this._breakPointStep = '';
    };
    ScrollEvent.prototype.resize = function() {

        var $floatLayer = $(spyWrap),
            floatPosition = defaultPosition,
            windowWidth = $(window).width(),
            eventSwitch = false;

        if( windowWidth + scrollBarWidth >= breakPoint ) {
            $floatLayer.css({'top':floatPosition,'bottom':'inherit','z-index':10});
            if( !eventSwitch ){
                $(window).on('scroll.spyButton', function(){
                    var scrollTop = $(window).scrollTop();
                    if (scrollTop >= 250) {
                        $floatLayer.css('top', '50%');
                    } else {
                        $floatLayer.css('top', floatPosition);
                    }
                });
            }
            eventSwitch = true;
        } else {
            eventSwitch = false;
            $(window).off('scroll.spyButton');
            $floatLayer.css({'top':'inherit','bottom':bottomPosition,'z-index':12});
        }
    };

    var scrollSpy = new ScrollEvent();

    $(document).ready(function(){
        scrollSpy.resize();
    });

    $(window).resize(function(){
        scrollSpy.resize();
    });
}
//배너 슬라이드
function bannerSlick() {

    var bannerSlick = $('.banner .slide_area').slick({
            prevArrow: '.prevBanner',
            nextArrow: '.nextBanner',
            dots: false,
            slidesToShow: 5,
            variableWidth: true,
            speed: 300,
            autoplay: true
        }),
        playStat = true;

    $('.banner .slideControl').on('click', function(){

        $(this).toggleClass("play");

        if( playStat ) {

            bannerSlick.slick('slickPause');
            $(this).html('배너 슬라이드 재생');

        } else {

            bannerSlick.slick('slickPlay');
            $(this).html('배너 슬라이드 정지');

        }
        playStat = !playStat;

    });

}
//하단 사이트 링크 모음
function toShowSiteLink(){

    var $linkTarget = $('.footerSiteLink'),
        $bindButton = $linkTarget.find('.linkBind'),
        $bindList = $linkTarget.find('> ul');

    $bindButton.on('click', function () {

        if($(this).hasClass('active')) {
            $(this).removeClass('active');
            $(this).attr('title','링크 목록 열기');
            $(this).next($bindList).fadeOut(100);
        } else {
            $linkTarget.find('.active').removeClass('active');
            $(this).addClass('active');
            $(this).attr('title','링크 목록 닫기');
            $linkTarget.find('.link_list').fadeOut(100);
            $(this).next($bindList).fadeIn(200);
        }

    });

}
//브라우저 스크롤바 넓이
function getScrollBarWidth() {

    var inner = document.createElement('p');
    inner.style.width = "100%";
    inner.style.height = "200px";

    var outer = document.createElement('div');
    outer.style.position = "absolute";
    outer.style.top = "0px";
    outer.style.left = "0px";
    outer.style.visibility = "hidden";
    outer.style.width = "200px";
    outer.style.height = "150px";
    outer.style.overflow = "hidden";
    outer.appendChild (inner);

    document.body.appendChild (outer);
    var w1 = inner.offsetWidth;
    outer.style.overflow = 'scroll';
    var w2 = inner.offsetWidth;
    if (w1 == w2) w2 = outer.clientWidth;

    document.body.removeChild (outer);

    return (w1 - w2);

}

function inputFile(){
    var $inputFileGroup = $('.inputFileGroup'),
        $fileButton = $inputFileGroup.find('.fileButton'),
        idx;

    $fileButton.on('click',function(e){
        idx = $fileButton.index(this);
        e.preventDefault();
        $inputFileGroup.find('#atchmnfl_'+idx).click();
    });
    $('.file-clear').on('click',function(){

        idx= $('.file-clear').index(this);

        $(this).css('visibility','hidden').prev().empty();

        var agent = navigator.userAgent.toLowerCase();

        if ( (navigator.appName == 'Netscape' && navigator.userAgent.search('Trident') != -1) || (agent.indexOf('mise') != -1) ) {
            $inputFileGroup.find('#atchmnfl_'+idx).replaceWith($inputFileGroup.find('#atchmnfl_'+idx).clone(true));
        } else {
            $inputFileGroup.find('#atchmnfl_'+idx).val('');
        }

        console.log($inputFileGroup.find('#atchmnfl_'+idx).val());

    })
}

function changeValue(obj) {

    var file = obj.value,
        arSplitUrl = file.split('\\'),
        nArLength = arSplitUrl.length,
        arFileName = arSplitUrl[nArLength-1];

    $(obj).prev('.file-name').find('.file-name-text').html(arFileName);
    $(obj).prev('.file-name').find('.file-clear').css('visibility','visible').focus();

}
/*
$(document).on('click','.file-clear',function(){
    console.log('test');
    $(this).prev().find('.file-name-text').html();
});*/
