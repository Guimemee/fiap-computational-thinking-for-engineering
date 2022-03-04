#define chA 11
#define chB 10
#define ledA 4
#define ledB 3

bool A,B;

void setup() {
  pinMode(chA, INPUT);
  pinMode(chB, INPUT);
  pinMode(ledA, OUTPUT);
  pinMode(ledB, OUTPUT);

  digitalWrite(ledA, LOW);
  digitalWrite(ledB, LOW);
}

void loop() {
  A=digitalRead(chA);
  if(A == 0){
    digitalWrite(ledA, HIGH);
  }else{
    digitalWrite(ledA, LOW);
  }

  B=digitalRead(chB);
  if(B == 0){
    digitalWrite(ledB, LOW);
  }else{
    digitalWrite(ledB, HIGH);
  }
}
