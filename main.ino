/* Proyecto de No-limits */
// para el servo
int 

void setup() {
	Serial.begin(9600);
}

void loop() {
	//aquí va el código principal
}

void ultrasonic() {
	
}

void motor_right() {
	
}

void motor_left() {
	
}

void servo() {
	
}

// Codigo para los motores (considerando la entrada de un pot) //
/* 
int pin2= 9;
int pin7= 10;
int pote= A0;

int valorpote;
int pwm1;
int pwm2;


void setup() {
pinMode (pin2,OUTPUT);
pinMode (pin7, OUTPUT);

}

void loop() {
  valorpote=analogRead(pote);
  pwm1 = map(valorpote,0,1023,0,255);
  pwm2 = map(valorpote,0,1023,255,0);

  analogWrite (pin2,pwm1);
  analogWrite (pin7,pwm2);

}
*/
