from flask import Flask, render_template, request
app=Flask(__name__)
@app.route('/',methods=['GET','POST'])
def home():
        if request.method=='POST':
                stress=int(request.form.get('stress'))
                breath=int(request.form.get('breath'))
                pee=int(request.form.get('pee'))
                skin=int(request.form.get('skin'))
                sleep=int(request.form.get('sleep'))
                stomach=int(request.form.get('stomach'))
                immune=int(request.form.get('immune'))
                recommended_scent=""
                if breath<=3 and skin<=3 and pee<=3 and sleep<=3 and stomach<=3 and immune<=3:
                         recommended_scent=['그레이프 푸르트','라벤더']
                elif skin>=4 and sleep>=4:
                        recommended_scent=['레몬그래스','스위트 오렌지','로즈마리']
                elif skin>=4:
                        recommended_scent=['레몬그래스','스위트 오렌지']
                elif sleep>=4:
                        recommended_scent=['로즈마리','스위트 오렌지']
                elif pee>=4 and breath>=4:
                        recommended_scent=['프랜컨센스','베르가못','유칼립투스']
                elif breath>=4:
                        recommended_scent=['시나몬','파인트리','유칼립투스']
                elif stomach>=4:
                        recommended_scent=['페퍼민트','라벤더']
                elif immune>=4:
                        recommended_scent=['티트리','그레이프 푸르트']
                return render_template('result.html',scent=recommended_scent)
        return render_template('index.html')
if __name__=='__main__':
    app.run(debug=True)