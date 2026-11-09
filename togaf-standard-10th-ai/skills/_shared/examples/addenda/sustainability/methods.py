# -*- coding: utf-8 -*-
"""Data-quality and qualitative checks; no new environmental accounting formula."""
DIMENSIONS={'战略','治理','业务/数据/应用/技术架构','文化','数字环境足迹度量','生态系统'}
def capability(rows,scoring_model=None):
 if len(rows)!=len(DIMENSIONS) or {r['dimension'] for r in rows}!=DIMENSIONS:raise ValueError('sustainability-dimension-gap')
 if scoring_model is not None:raise ValueError('project-scoring-model-review-required; qualitative procedure does not validate numeric scoring')
 if scoring_model is None and any(r['rating']!='not-scored' for r in rows):raise ValueError('unsourced-maturity-rating')
 return {'dimensions':len(rows),'scoring':'not-scored' if scoring_model is None else 'project-model-required','gaps':[r['gap'] for r in rows if r['gap'] not in ['none','closed-in-fixture']]}

def dual(rows):
 if {r['entry_point'] for r in rows}!={'use','infrastructure'}:raise ValueError('dual-entry-missing-entry')
 for r in rows:
  if not r.get('use_id') or len(r.get('application_data_path',[]))<2 or not r.get('infrastructure_id'):raise ValueError('dual-entry-trace-gap')
  if set(r['constraints'])!={'use','data','application-development','infrastructure'}:raise ValueError('constraint-category-gap')
 return {'use_priorities':[r['use_id'] for r in rows if r['entry_point']=='use'],'infrastructure_priorities':[r['infrastructure_id'] for r in rows if r['entry_point']=='infrastructure'],'conflicts':[r['infrastructure_id'] for r in rows if 'conflict' in r['status']],'emissions_calculated':False}

def education(rows,total_staff):
 allstaff=[r for r in rows if r['audience']=='全部员工']
 if len(allstaff)!=1 or allstaff[0]['population']!=total_staff:raise ValueError('all-staff-coverage-gap')
 if not any(r['audience']=='采购人员' for r in rows):raise ValueError('procurement-education-gap')
 return {'all_staff_scope':total_staff,'overlapping_role_groups':len(rows)-1,'verified_groups':[r['audience'] for r in rows if r['status']=='application-verified-in-fixture'],'population_sum':'not-performed; overlapping audiences'}

def factors(rows):
 for r in rows:
  if not all(r.get(k) for k in ['unit','period','geography','lifecycle_boundary','source_version','source_locator']):raise ValueError('carbon-data-metadata-gap')
  if r['data_kind']=='equipment-embodied' and '/year' in r['unit']:raise ValueError('boundary-unit-conflict')
  if r['data_kind']=='datacenter-activity-intensity' and not r['allocation_basis']:raise ValueError('missing-service-allocation')
 return {'rows':len(rows),'versions':[r['source_version'] for r in rows],'totals_calculated':False,'grid_factors':[r['value'] for r in rows if r['data_kind']=='grid-emission-factor']}

def procurement(rows):
 for r in rows:
  if r['recommendation']=='selected' and ('抵消后' in r['lifecycle_evidence'] or not r['whole_life_tco'] or r['gaps']):raise ValueError('procurement-transparency-gap')
 return {'options':len(rows),'open_gaps':sum(len(r['gaps']) for r in rows),'selection':'not-made','scores':'none; no sourced weighting'}

def cloud(v,keys):
 data=v['data']
 if set(data)!=set(keys):raise ValueError('cloud-field-set-gap')
 if not v.get('allocation_basis'):raise ValueError('cloud-allocation-gap')
 if v.get('requested_aggregation') in ['sum-scope2','market-plus-location']:raise ValueError('scope2-bases-not-additive')
 if v.get('requested_aggregation') in ['total-plus-equipment','net-offsets']:raise ValueError('subset-or-offset-not-additive')
 periods=v['period_by_field']
 if any(periods.get(k)!=data['period'] for k in keys):raise ValueError('cloud-period-mismatch')
 numeric=['electricity_consumption_kwh','renewable_electricity_purchased_kwh','scope2_market_based_kgco2e','scope2_location_based_kgco2e','pue','total_scope3_kgco2e','digital_equipment_scope3_kgco2e','carbon_credits_offsets_kgco2e','digital_waste_kg','recycled_digital_waste_kg','stored_data_gb_including_replication','network_traffic_gb']
 for key in numeric:
  value=data[key]
  if value is not None and (not isinstance(value,(int,float)) or isinstance(value,bool) or value<0):raise ValueError('cloud-numeric-value-invalid:'+key)
 total=data['total_scope3_kgco2e'];subset=data['digital_equipment_scope3_kgco2e']
 if total is not None and subset is not None and subset>total:raise ValueError('scope3-subset-exceeds-total')
 if v.get('replicas_included') is not True:raise ValueError('cloud-replication-gap')
 water=data['water_consumption']
 if not isinstance(water,dict) or not all(k in water for k in ['value','unit','lifecycle_stage']):raise ValueError('cloud-water-boundary-gap')
 return {'source_fields':len(keys),'quantitative_gaps':[k for k in numeric if data[k] is None],'scope2_bases':'parallel-alternatives; no sum','scope3_equipment_relation':'subset-not-added','credits_offsets':'separate-not-netted','supplier_scope_labels':'consumer classification requires separate analysis','water_gap':water.get('gap'),'replicas_included':True,'emissions_total':'not-calculated-by-contract'}

def export_grid_factor(r):
 if r['data_kind']!='grid-emission-factor' or r['unit']!='kgCO2e/kWh':raise ValueError('not-an-electricity-emission-factor')
 return {'id':'example-'+r['source_version'].replace('/','-'),'value':r['value'],'numerator_unit':'kgCO2e','denominator_unit':'kWh','period':r['period'],'geography':r['geography'],'evidence':[r['source_locator']],'origin':'fictional-project-scenario; not a default factor'}
