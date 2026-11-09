"""Repair figure-scoped asset evidence; a shared MD path is never an identity."""
import hashlib,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
def read(path):return json.loads(path.read_text())
def dump(path,value):path.write_text(json.dumps(value,ensure_ascii=False,indent=2)+'\n')
def identity(figure,asset):
    locator=asset.get('locator')
    if locator is None and asset.get('kind')=='label_table':locator={'lines':figure.get('md_locator',{}).get('label_table_lines',[])}
    return {'figure_id':figure['id'],'kind':asset.get('kind'),'path':asset['path'],'locator':locator or {'whole_asset':True}}
def main():
    p=ROOT/'evidence-registry.json';registry=read(p);actions=[]
    for figure in registry['figures']:
        fid=figure['id'];reportpath=ROOT/'reviews/figure-verification'/(fid.replace('/','-')+'.json')
        report=read(reportpath) if reportpath.exists() else None
        if report and report.get('figure_id')!=fid:raise ValueError('Wrong figure report '+str(reportpath))
        for asset in figure.get('assets',[]):
            old=asset.get('independent_verification');key=identity(figure,asset)
            if not old:continue
            oldpath=ROOT/old.get('evidence','missing');oldreport=read(oldpath) if oldpath.is_file() else None
            if oldreport and oldreport.get('figure_id')==fid:
                old['asset_identity']=key;continue
            candidates=[a for a in (report or {}).get('assets',[]) if a.get('path')==asset['path'] and a.get('kind')==asset.get('kind')]
            # A report is already figure-scoped. A unique kind/path within that
            # figure binds to its local table locator, never to another MD row.
            asset.setdefault('verification_link_history',[]).append({'rejected':old,'reason':'report figure differs from asset figure; shared document path is not sufficient identity'})
            if len(candidates)==1:
                observed=candidates[0];asset['independent_verification']={'evidence':str(reportpath.relative_to(ROOT)),'asset_identity':key,**{k:observed[k] for k in ['verdict','actually_shows','issues_zh'] if k in observed}}
                action='rebound-to-unique-figure-kind-locator'
            else:
                asset.pop('independent_verification',None);asset['verification_link_status']='not-independently-verified-at-this-locator';action='unrelated-verdict-withdrawn-no-matching-report'
            actions.append({'asset_identity':key,'action':action,'previous_report':old.get('evidence'),'matching_report':str(reportpath.relative_to(ROOT)) if len(candidates)==1 else None})
    package=read(ROOT/'capability-addenda/metadata-repair.json')
    for name,base in package['source_assets'].items():
        figure=next(f for f in registry['figures'] if f['id']==base['figure_id'])
        asset={'path':base['path'],'path_base':'skills/_shared','kind':'recovered_source_crop' if name!='application' else 'bundled_source_copy','exists':True,'sha256':base['sha256'],'locator':{'pdf_page':base['pdf_page'],'figure_id':base['figure_id']},'source_version':base['source_version'],'source_pdf_sha256':base['source_pdf_sha256'],'current_visual_review':'opened-source-structure-and-readable-labels','verification_scope':base['verification_scope'],'evidence':'reviews/metadata-independent-review.json'}
        same=next((a for a in figure['assets'] if a['path']==asset['path'] and a['kind']==asset['kind']),None)
        if same:same.update(asset)
        else:figure['assets'].append(asset)
        if name=='application':
            figure['profile_ids']=list(dict.fromkeys(figure.get('profile_ids',[])+['metadata-application-function-map']))
            figure['disposition']='source-derived-view-profile';figure['disposition_reason']='图5-2同时支持元数据需求方法和独立应用功能视图；完整表5-2为可移植定义依据。'
        if name=='solution':
            figure['source_status']='trusted-pdf-crop-bundled-original-local-assets-remain-wrong'
            figure['asset_limitation']='可信PDF第25页图4-4裁图现已保存在skills内部；原本地英文/中文PNG及标签表仍是图4-3。嵌入产品界面细小标签未逐字核对。'
    correction=ROOT/'reviews/source-audit-corrections.json';c=read(correction)
    for item in c['observations']:
        if item['figure_id']=='G234/fig4-4':
            item['historical_opened_pdf_crop']=item.get('historical_opened_pdf_crop',item['opened_pdf_crop'])
            item['opened_pdf_crop']='reviews/source-template-bases/G234-fig4-4-p25-0.png';item['crop_path_base']='skills/_shared';item['crop_sha256']=package['source_assets']['solution']['sha256']
            item['registry_correction_zh']='可信图4-4已从英文PDF第25页恢复到skills内部并实际打开；原英文PNG、中文PNG及标签表仍属图4-3，保留冲突。裁图、版本、哈希与原始错图并列登记。'
    dump(correction,c);dump(p,registry)
    report=ROOT/'reviews/source-asset-link-repair.json';prior=read(report) if report.exists() else {'actions':[]};keys={json.dumps(x['asset_identity'],sort_keys=True):x for x in prior['actions']}
    keys.update({json.dumps(x['asset_identity'],sort_keys=True):x for x in actions})
    dump(report,{'identity_rule':'figure_id + kind + path + local locator; never MD path alone','actions':list(keys.values()),'recovered_assets':package['source_assets'],'original_materials_unchanged':True,'notice':'Withdrawing an unrelated verdict does not verify the correct table. Missing matching reports remain explicitly unverified.'})
    print({'new_repairs':len(actions),'total_repairs':len(keys),'bundled_assets':len(package['source_assets'])})
if __name__=='__main__':main()
