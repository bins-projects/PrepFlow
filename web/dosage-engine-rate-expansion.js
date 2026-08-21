(() => {
  const E=window.DosageEngine;if(!E)return;
  const previous=E.generate.bind(E),pick=a=>a[Math.floor(Math.random()*a.length)],round=E.round;
  const q=(key,type,prompt,answer,unit,formula,note,solution,tolerance=.05,vars={})=>({key,type,prompt,answer,unit,formula,note,solution,tolerance,vars});
  const randDec=(min,max,p=1)=>round(min+Math.random()*(max-min),p);

  function rateBased(d='standard'){
    const kind=pick(['amiodarone','lidocaine','diltiazem','nicardipine','magnesium']);
    if(kind==='amiodarone'){
      const order=pick([0.5,1]),bag=pick([[450,250],[900,500]]),conc=bag[0]/bag[1],hourly=order*60,a=round(hourly/conc,1);
      return q('amount-hour','Rate-based infusion (mg/min, mg/hr, or g/hr)',`Amiodarone is ordered at ${order} mg/min. The IV contains ${bag[0]} mg in ${bag[1]} mL. What pump rate is required?`,a,'mL/hr','(mg/min × 60 min/hr) ÷ mg/mL = mL/hr','Convert mg/min to mg/hr before dividing by concentration.',`${order} × 60 = ${hourly} mg/hr; ${bag[0]} ÷ ${bag[1]} = ${round(conc,2)} mg/mL; ${hourly} ÷ ${round(conc,2)} = ${a} mL/hr`,.05,{drug:'amiodarone',order,orderUnit:'mg/min',bagAmt:bag[0],bagMl:bag[1]});
    }
    if(kind==='lidocaine'){
      const order=pick([1,2,3,4]),bag=pick([[1000,1000],[2000,1000]]),conc=bag[0]/bag[1],hourly=order*60,a=round(hourly/conc,1);
      return q('amount-hour','Rate-based infusion (mg/min, mg/hr, or g/hr)',`Lidocaine is ordered as a continuous IV infusion at ${order} mg/min for ventricular arrhythmia management. The IV contains ${bag[0]} mg in ${bag[1]} mL. What pump rate is required?`,a,'mL/hr','(mg/min × 60 min/hr) ÷ mg/mL = mL/hr','Convert mg/min to mg/hr, then divide by the infusion concentration.',`${order} × 60 = ${hourly} mg/hr; ${bag[0]} ÷ ${bag[1]} = ${round(conc,2)} mg/mL; ${hourly} ÷ ${round(conc,2)} = ${a} mL/hr`,.05,{drug:'lidocaine',order,orderUnit:'mg/min',bagAmt:bag[0],bagMl:bag[1]});
    }
    if(kind==='diltiazem'){
      const order=d==='easy'?pick([5,10,15]):pick([5,6,7,8,9,10,11,12,13,14,15]),bag=[125,125],conc=1,a=round(order/conc,1);
      return q('amount-hour','Rate-based infusion (mg/min, mg/hr, or g/hr)',`Diltiazem is ordered as a continuous infusion at ${order} mg/hr. The pharmacy-prepared IV contains 125 mg in 125 mL. What pump rate is required?`,a,'mL/hr','mg/hr ÷ mg/mL = mL/hr','The order is already per hour; divide by the prepared concentration.',`125 ÷ 125 = 1 mg/mL; ${order} ÷ 1 = ${a} mL/hr`,.05,{drug:'diltiazem',order,orderUnit:'mg/hr',bagAmt:125,bagMl:125});
    }
    if(kind==='nicardipine'){
      const order=pick([5,7.5,10,12.5,15]),bag=pick([[25,250],[50,250]]),conc=bag[0]/bag[1],a=round(order/conc,1);
      return q('amount-hour','Rate-based infusion (mg/min, mg/hr, or g/hr)',`Nicardipine is ordered as a continuous IV infusion at ${order} mg/hr. The prepared infusion contains ${bag[0]} mg in ${bag[1]} mL. What pump rate is required?`,a,'mL/hr','mg/hr ÷ mg/mL = mL/hr','The order is already per hour; divide by the infusion concentration.',`${bag[0]} ÷ ${bag[1]} = ${round(conc,2)} mg/mL; ${order} ÷ ${round(conc,2)} = ${a} mL/hr`,.05,{drug:'nicardipine',order,orderUnit:'mg/hr',bagAmt:bag[0],bagMl:bag[1]});
    }
    const order=d==='easy'?pick([1,1.5,2]):pick([1,1.25,1.5,1.75,2]),bag=pick([[20,500],[40,1000]]),conc=bag[0]/bag[1],a=round(order/conc,1);
    return q('amount-hour','Rate-based infusion (mg/min, mg/hr, or g/hr)',`Magnesium sulfate is ordered at ${order} g/hr by continuous IV infusion. The IV contains ${bag[0]} g in ${bag[1]} mL. What pump rate is required?`,a,'mL/hr','g/hr ÷ g/mL = mL/hr','The order is already per hour.',`${bag[0]} ÷ ${bag[1]} = ${round(conc,4)} g/mL; ${order} ÷ ${round(conc,4)} = ${a} mL/hr`,.05,{drug:'magnesium sulfate',order,orderUnit:'g/hr',bagAmt:bag[0],bagMl:bag[1]});
  }

  function mcgKgMin(d='standard'){
    if(Math.random()<0.38){
      const kg=d==='easy'?pick([50,60,70,80,90]):randDec(48,92,1),dose=d==='easy'?pick([50,100,150,200]):pick([50,75,100,125,150,175,200]),bagMcg=2500000,bagMl=250,conc=bagMcg/bagMl,a=round(dose*kg*60/conc,1);
      return q('mcg-kg-minute','mcg/kg/min infusion',`A ${kg}-kg patient is receiving esmolol for supraventricular tachycardia at ${dose} mcg/kg/min. The IV contains 2,500 mg in ${bagMl} mL. What pump rate is required?`,a,'mL/hr','(mcg/kg/min × kg × 60 min/hr) ÷ mcg/mL = mL/hr','Convert the bag amount to mcg, calculate the weight-based hourly dose, then divide by concentration.',`${dose} × ${kg} × 60 = ${round(dose*kg*60,1)} mcg/hr; 2,500,000 ÷ ${bagMl} = ${conc} mcg/mL; ${round(dose*kg*60,1)} ÷ ${conc} = ${a} mL/hr`,.05,{drug:'esmolol',kg,dose,bagMcg,bagMl});
    }
    return previous('mcg-kg-minute',d);
  }

  function mcgKgHour(d='standard'){
    const kg=d==='easy'?pick([50,60,70,80,90]):randDec(48,92,1),dose=d==='easy'?pick([0.2,0.4,0.6]):pick([0.2,0.3,0.4,0.5,0.6,0.7]),bagMcg=200,bagMl=50,conc=bagMcg/bagMl,a=round(dose*kg/conc,1);
    return q('mcg-kg-hour','mcg/kg/hr infusion',`A ${kg}-kg adult is receiving dexmedetomidine for ICU sedation at ${dose} mcg/kg/hr. The IV contains ${bagMcg} mcg in ${bagMl} mL. What pump rate is required?`,a,'mL/hr','(mcg/kg/hr × kg) ÷ mcg/mL = mL/hr','Because the order is already per hour, do not multiply by 60.',`${dose} × ${kg} = ${round(dose*kg,2)} mcg/hr; ${bagMcg} ÷ ${bagMl} = ${conc} mcg/mL; ${round(dose*kg,2)} ÷ ${conc} = ${a} mL/hr`,.05,{drug:'dexmedetomidine',kg,dose,bagMcg,bagMl,orderUnit:'mcg/kg/hr'});
  }

  const oldGenerate=E.generate.bind(E);
  E.generate=(key,d='standard')=>key==='amount-hour'?rateBased(d):key==='mcg-kg-minute'?mcgKgMin(d):key==='mcg-kg-hour'?mcgKgHour(d):oldGenerate(key,d);
  if(!E.types.some(t=>t.key==='mcg-kg-hour')) E.types.push({key:'mcg-kg-hour',label:'mcg/kg/hr infusion'});
  if(!E.formulaReview.some(x=>x[0]==='mcg/kg/hr infusion')) E.formulaReview.push(['mcg/kg/hr infusion','(mcg/kg/hr × kg) ÷ mcg/mL = mL/hr']);
  E.semanticSignature=(x)=>{
    const v=x?.vars||{};
    if(x?.key==='amount-hour'&&v.drug&&v.bagAmt&&v.bagMl){const conc=round(v.bagAmt/v.bagMl,4);return `${x.key}|${v.drug}|${v.orderUnit}|${v.order}|${conc}`;}
    if(x?.key==='mcg-kg-minute'&&v.drug&&v.bagMcg&&v.bagMl){const conc=round(v.bagMcg/v.bagMl,4);return `${x.key}|${v.drug}|${v.dose}|${v.kg}|${conc}`;}
    if(x?.key==='mcg-kg-hour'&&v.drug&&v.bagMcg&&v.bagMl){const conc=round(v.bagMcg/v.bagMl,4);return `${x.key}|${v.drug}|${v.dose}|${v.kg}|${conc}`;}
    return `${x?.key||''}|${String(x?.prompt||'').toLowerCase().replace(/\s+/g,' ').trim()}`;
  };
  E.version=5;
})();