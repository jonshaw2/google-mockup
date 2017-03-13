$(document).ready(function(){
  var current_deck = new Deck();
  console.log(current_deck.currentDeck);
  current_deck.shuffle();
  console.log(current_deck.currentDeck);

  // var dealer_hand = new Hand();
  // var player_hand = new Hand();

  $('#deal-button').click(function(){

    // deal();
    // updateScore();

    $('.hit_button').css('pointer-events', 'auto');
    $('.hit_button').css('background-color', 'lightblue');
    $('.stand_button').css('pointer-events', 'auto');
    $('.stand_button').css('background-color', 'lightblue');
    $('.deal_button').css('pointer-events', 'none');
    $('.deal_button').css('background-color', 'black');
  });

  $('#hit-button').click(function(){

    dealCard();
    updateScore();
    bust();

  });

  function Card(points, suits){
    this.point = points;
    this.suit = suits;


    Card.prototype.getImageUrl = function() {
      var returnCard = this.point;
      if (this.point === 11){
        returnCard ="jack";
      }
      else if (this.point === 12){
        returnCard ="queen";
      }
      else if (this.point === 13){
        returnCard = "king";
      }
      else if (this.point === 1){
        returnCard = "ace";
      }
      imageUrl = 'images/' + returnCard + '_of_' + this.suit+'.png';
      return imageUrl;
    };
  }

  function Hand(){
    this.cardsInHand = [];

    Hand.prototype.addCard = function(card){
      this.cardsInHand.push(card);
    };

    Hand.prototype.getPoints = function(){
      var sumPoints = this.cardsInHand.reduce(function(a, b){
        if (b.point>10){
          b.point=10;
        }
        return a + b.point;
      },0);
      return sumPoints;
    };
  }

  function Deck(){
    this.currentDeck = [];
    var suits = ['club','diamond','heart','spade'];
    var points = [1,2,3,4,5,6,7,8,9,10,11,12,13];
    for (i=0; i<points.length;i++){
      for (j=0; j<suits.length;j++){
        this.currentDeck.push(new Card(points[i],suits[j]));
      }
    }


    Deck.prototype.draw = function() {
      return this.currentDeck.pop();
    };

    Deck.prototype.shuffle = function() {
      var tempDeck = [];
      while (this.currentDeck.length > 0){
        randomCard = Math.floor(Math.random()*(this.currentDeck.length-1));
        splice = this.currentDeck.splice(randomCard,1);
        tempDeck.push(splice[0]);
      }
      this.currentDeck = tempDeck;
    };

    Deck.prototype.numCardsLeft = function(){
      return this.currentDeck.length;
    };

  }


});
