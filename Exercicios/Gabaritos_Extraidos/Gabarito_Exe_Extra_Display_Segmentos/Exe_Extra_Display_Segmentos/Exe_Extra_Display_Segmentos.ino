#define Seg_A 2
#define Seg_B 3
#define Seg_C 4
#define Seg_D 9
#define Seg_E 10
#define Seg_F 12
#define Seg_G 11

char entrada;

void setup() {
  Serial.begin(9600);
  
  pinMode(Seg_A, OUTPUT);
  pinMode(Seg_B, OUTPUT);
  pinMode(Seg_C, OUTPUT);
  pinMode(Seg_D, OUTPUT);
  pinMode(Seg_E, OUTPUT);
  pinMode(Seg_F, OUTPUT);
  pinMode(Seg_G, OUTPUT);

  digitalWrite(Seg_A, LOW);
  digitalWrite(Seg_B, LOW);
  digitalWrite(Seg_C, LOW);
  digitalWrite(Seg_D, LOW);
  digitalWrite(Seg_E, LOW);
  digitalWrite(Seg_F, LOW);
  digitalWrite(Seg_G, LOW);
}

void loop() {
  Serial.println("Escolha pelo Menu:");
  Serial.println("a ou A para 0");
  Serial.println("b ou B para 1");
  Serial.println("c ou C para 2");
  Serial.println("d ou D para 3");
  Serial.println("e ou E para 4");
  Serial.println("f ou F para 5");
  Serial.println("g ou G para 6");
  Serial.println("h ou H para 7");
  Serial.println("i ou I para 8");
  Serial.println("j ou J para 9");
  while(Serial.available()==0);
  entrada=Serial.read();

  switch(entrada){
    case 'a':
    case 'A':
      digitalWrite(Seg_A, HIGH);
      digitalWrite(Seg_B, HIGH);
      digitalWrite(Seg_C, HIGH);
      digitalWrite(Seg_D, HIGH);
      digitalWrite(Seg_E, HIGH);
      digitalWrite(Seg_F, HIGH);
      digitalWrite(Seg_G, LOW);
    break;
    case 'b':
    case 'B':
      digitalWrite(Seg_A, LOW);
      digitalWrite(Seg_B, HIGH);
      digitalWrite(Seg_C, HIGH);
      digitalWrite(Seg_D, LOW);
      digitalWrite(Seg_E, LOW);
      digitalWrite(Seg_F, LOW);
      digitalWrite(Seg_G, LOW);
    break;
    case 'c':
    case 'C':
      digitalWrite(Seg_A, HIGH);
      digitalWrite(Seg_B, HIGH);
      digitalWrite(Seg_C, LOW);
      digitalWrite(Seg_D, HIGH);
      digitalWrite(Seg_E, HIGH);
      digitalWrite(Seg_F, LOW);
      digitalWrite(Seg_G, HIGH);
    break;
    case 'd':
    case 'D':
      digitalWrite(Seg_A, HIGH);
      digitalWrite(Seg_B, HIGH);
      digitalWrite(Seg_C, HIGH);
      digitalWrite(Seg_D, HIGH);
      digitalWrite(Seg_E, LOW);
      digitalWrite(Seg_F, LOW);
      digitalWrite(Seg_G, HIGH);
    break;
    case 'e':
    case 'E':
      digitalWrite(Seg_A, LOW);
      digitalWrite(Seg_B, HIGH);
      digitalWrite(Seg_C, HIGH);
      digitalWrite(Seg_D, LOW);
      digitalWrite(Seg_E, LOW);
      digitalWrite(Seg_F, HIGH);
      digitalWrite(Seg_G, HIGH);
    break;
    case 'f':
    case 'F':
      digitalWrite(Seg_A, HIGH);
      digitalWrite(Seg_B, LOW);
      digitalWrite(Seg_C, HIGH);
      digitalWrite(Seg_D, HIGH);
      digitalWrite(Seg_E, LOW);
      digitalWrite(Seg_F, HIGH);
      digitalWrite(Seg_G, HIGH);
    break;
    case 'g':
    case 'G':
      digitalWrite(Seg_A, HIGH);
      digitalWrite(Seg_B, LOW);
      digitalWrite(Seg_C, HIGH);
      digitalWrite(Seg_D, HIGH);
      digitalWrite(Seg_E, HIGH);
      digitalWrite(Seg_F, HIGH);
      digitalWrite(Seg_G, HIGH);
    break;
    case 'h':
    case 'H':
      digitalWrite(Seg_A, HIGH);
      digitalWrite(Seg_B, HIGH);
      digitalWrite(Seg_C, HIGH);
      digitalWrite(Seg_D, LOW);
      digitalWrite(Seg_E, LOW);
      digitalWrite(Seg_F, LOW);
      digitalWrite(Seg_G, LOW);
    break;
    case 'i':
    case 'I':
      digitalWrite(Seg_A, HIGH);
      digitalWrite(Seg_B, HIGH);
      digitalWrite(Seg_C, HIGH);
      digitalWrite(Seg_D, HIGH);
      digitalWrite(Seg_E, HIGH);
      digitalWrite(Seg_F, HIGH);
      digitalWrite(Seg_G, HIGH);
    break;
    case 'j':
    case 'J':
      digitalWrite(Seg_A, HIGH);
      digitalWrite(Seg_B, HIGH);
      digitalWrite(Seg_C, HIGH);
      digitalWrite(Seg_D, LOW);
      digitalWrite(Seg_E, LOW);
      digitalWrite(Seg_F, HIGH);
      digitalWrite(Seg_G, HIGH);
    break;
    default:
      Serial.println("Opcao Invalida!");
  }
  
}