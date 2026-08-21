(() => {
  const E=window.DosageEngine;if(!E)return;
  const wanted=[
    {key:'medication-dosing',label:'Medication Dosing',description:'Medication amounts, reconstitution, and electrolyte volumes.',types:['basic-dose','reconstitution','meq-ml']},
    {key:'pediatric-dosing',label:'Pediatric Dosing',description:'Weight-based, safe-range, and divided pediatric doses.',types:['weight-dose','peds-safe-range','daily-divided']},
    {key:'infusion-rates',label:'Infusion Rates',description:'Pump, gravity, unit-based, and weight-based infusion-rate calculations.',types:['mlhr-hours','mlhr-minutes','gtt-volume-time','gtt-from-mlhr','mlhr-from-gtt','units-hour','mcg-minute','mcg-kg-minute','mcg-kg-hour','amount-hour']},
    {key:'iv-time-volume',label:'IV Time & Volume',description:'Infusion duration and completion-time calculations.',types:['infusion-time','completion-time']}
  ];
  const live=new Map(E.types.map(t=>[t.key,t]));
  const families=wanted.map(f=>({...f,types:f.types.filter(k=>live.has(k))})).filter(f=>f.types.length);
  const typeLabel=key=>live.get(key)?.label||key;
  const familyForType=key=>families.find(f=>f.types.includes(key))||null;
  E.families=families;
  E.typeLabel=typeLabel;
  E.familyForType=familyForType;
})();