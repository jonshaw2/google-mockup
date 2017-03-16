$(document).ready(function(){
    $("#portfolio").click(function(){
      home_layout();
      portfolio_layout();
    });

    $("#home").click(function(){
      home_layout();

    });

    $("#about").click(function() {
      home_layout();
      about_layout();

    });
    function portfolio_layout(){
      $(".mid_content").css('opacity','0');
      $(".portfolio").css('opacity', '1');
      $(".top").css('height', '17vh');
      $(".middle").css('margin','17vh 0 0 0');
    }

    function home_layout(){
      $(".mid_content").css('opacity','1');
      $(".portfolio").css('opacity','0');
      $(".about").css('opacity','0');
      $(".top").css('height', '34vh');
      $(".middle").css('margin','34vh 0 0 0');

    }
    function about_layout(){
      $(".mid_content").css('opacity','0');
      $(".about").css('opacity', '1');
      $(".top").css('height', '17vh');
      $(".middle").css('margin','17vh 0 0 0');


    }

    function snow_background(){


        this.sheight = [0,0,0,0,0,0,0,0,0,0];
        this.swidth = [0,0,0,0,0,0,0,0,0,0];
        this.snowCount = [0,0,0,0,0,0,0,0,0,0];
        this.speed = [0,0,0,0,0,0,0,0,0,0];
        for(var i=0; i<this.sheight.length;i++){
          this.swidth[i]=Math.floor(Math.random()*window.innerWidth-200)+100;
          this.speed[i]=Math.floor(Math.random()*2)+1;
          $(".background").append('<img class="snow'+i+'" src="image/snow.png">');

          $(".snow"+i).css('position','absolute');
          $(".snow"+i).css('opacity','.2');
          $(".snow"+i).css('width','25px');
          $(".snow"+i).css('margin',this.sheight[i] +' 0 0 -9000px');

          this.snowCount[i] = i;


        }

        var counter = 0;
        callingSnow();

        function callingSnow(){
          setTimeout(function(){

            this.snowCount[counter] = counter;

            snowing(this.sheight[counter], this.swidth[counter], this.snowCount[counter], this.speed[counter]);

            if (counter <= 10){
              callingSnow();
              counter += 1;
            }
            else{
            }
          }, 1000*counter+1);

        }
      function snowing(sheight, swidth, snowCount, speed){


        console.log(snowCount);
        if (sheight <= window.innerHeight-100){

          sheight += speed;


          $(".snow"+snowCount).css('margin',sheight + 'px 0 0 '+swidth+'px');
          setTimeout(function(){
            snowing(sheight, swidth, snowCount, speed);
          }, 10);
        }
        else{
          sheight = 0;
          swidth = Math.floor(Math.random()*window.innerWidth-200)+100;
          speed = Math.floor(Math.random()*2)+1;
          snowing(sheight, swidth, snowCount, speed);


        }

      }
    }
  snow_background();
});
