import math

while True:
  try:
    print(">>>感谢小翁与我互撅!")
    height=float(input(">>>请撅入你的身高(m)："))
    weight=float(input(">>>请撅入你的体重(kg)："))
    break
  except ValueError:
    print(">>>homo特有的听不懂人话，给我输入数字啊，三回啊三回（全恼")
    continue

bmi=round(weight/(math.pow(height,2)),2)
print("你的BMI已脱出：",bmi)

if bmi<18.5:
  print("你的BMI偏瘦，给我多食雪啊（恼")

elif bmi>=18.5 and bmi<=24.9:
  print("你的BMI正常，压力马斯内（赞赏")

elif bmi>=25 and bmi<=29.9:
  print("你的BMI偏胖，homo特有的圆润（确信")

elif bmi>=30 and bmi<=34.9:
  print("你的BMI肥胖，你改悔罢（无慈悲")

elif bmi>=35 and bmi<39.9:
  print("你的BMI重度肥胖，鸭蛋莫鸭蛋，牡蛎莫牡蛎（悲")

else:
  print("你的BMI极重度肥胖，哼，哼，哼，啊啊啊啊啊啊啊啊啊啊啊啊（撅望")

#Designed by SD