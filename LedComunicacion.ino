
//Programa para LED opencv
  
void setup()
{
  
   pinMode(8, OUTPUT); //establecemos el pin 8 como salida
   pinMode(9, OUTPUT); //establecemos el pin 9 como salida
   Serial.begin(9600); //inicializamos Serial
}
  
void loop()
{
  //Verificamos el envio de datos
   if (Serial.available() > 0)
   {
    //Depende el color en el caso  enciende los led
      switch(Serial.read())
      {
        
      //Apagamos todos o amarillo
      case '0': 
                digitalWrite(8,LOW);
                digitalWrite(9,LOW);
              break;
      //Enciende el led verde
      case '1':
               digitalWrite(9,HIGH);
              break;   
      //Enciende el led rojo
      case '2':
               digitalWrite(8,HIGH);
              break;
        
      default: break;
      }
   }
}
