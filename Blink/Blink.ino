int button0 = 2;
int button1 = 3;
int button2 = 4;
int button3 = 5;
int count0 = 0, count1 = 0, count2 = 0, count3 = 0;
int a, b, c, d;

void setup()
{
  pinMode(button0, INPUT);
  pinMode(button1, INPUT);
  pinMode(button2, INPUT);
  pinMode(button3, INPUT);
  Serial.begin(19200);
}

void loop()
{
  a = digitalRead(button0);
  b = digitalRead(button1);
  c = digitalRead(button2);
  d = digitalRead(button3);
  if (a == 0)
  {
    if (count0 == 0)
    {
      count0 = 1;
      Serial.print("right");
    }
  }
  else
  {
    if (count0 == 1)
    {
      count0 = 0;
    }
  }
  if (b == 0)
  {
    if (count1 == 0)
    {
      count1 = 1;
      Serial.print("left");
    }
  }
  else
  {
    if (count1 == 1)
    {
      count1 = 0;
    }
  }
  if (c == 0)
  {
    if (count2 == 0)
    {
      count2 = 1;
      Serial.print("ok");
    }
  }
  else
  {
    if (count2 == 1)
    {
      count2 = 0;
    }
  }
  if (d == 0)
  {
    count3 += 1;
    if (count3 == 1)
    {
      Serial.print("mode");
    }
    else if (count3 == 30)
    {
      Serial.print("end");
    }
  }
  else
  {
    if (count3 != 0)
    {
      count3 = 0;
    }
  }
  delay(100);
}
