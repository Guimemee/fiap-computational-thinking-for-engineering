//Gabarito Exe 1 do Arq 8

int opcao,op1,op1c,op1d,op1u,op2,op2c,op2d,op2u;
float r;

void setup() {
  Serial.begin(9600);
}

void loop() {
  Serial.println("Informe a operacao desejada:");
  Serial.println("1 para adicao");
  Serial.println("2 para subtracao");
  Serial.println("3 para multiplicacao");
  Serial.println("4 para divisao");
  while(Serial.available()==0);
  opcao=Serial.read();
  opcao = opcao - 48;
  
  Serial.println("Para a operacao escolhida, informe dois operandos: ");
  Serial.println("Operando 1");
  while(Serial.available()==0);
  op1c=Serial.read();
  op1c = op1c - 48;
  while(Serial.available()==0);
  op1d=Serial.read();
  op1d = op1d - 48;
  while(Serial.available()==0);
  op1u=Serial.read();
  op1u = op1u - 48;
  
  op1 = op1c*100+op1d*10+op1u;
  
  Serial.println("Operando 2");
  while(Serial.available()==0);
  op2c=Serial.read();
  op2c = op2c - 48;
  while(Serial.available()==0);
  op2d=Serial.read();
  op2d = op2d - 48;
  while(Serial.available()==0);
  op2u=Serial.read();
  op2u = op2u - 48;
  
  op2 = op2c*100+op2d*10+op2u;
  
  switch(opcao){
    case 1:
      r = op1 + op2;
    break;
    case 2:
      r = op1 - op2;
    break;
    case 3:
      r = op1 * op2;
    break;
    case 4:
      r = op1 / op2;
    break;
    default:
      Serial.println("Entrada invalida!");
  }
  
  Serial.println("Resultado: ");
  Serial.println(r);
      
}
