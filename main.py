import streamlit as st
import numpy as np
import pandas as pd
import matplotlib as plt
import altair as alt
import seaborn as sns
import streamlit.components.v1 as components
import time

# bootstrap 4 collapse example
height = st.sidebar.slider(
    '高さを調整してください', 0, 10000 ,500
)
components.html(
    """
    <p style="page-break-before:always; line-height:0.75pt; width:100%; font-size:0.75pt;"></p><p class="smt_head3" style="orphans:0;widows:0;">(3) 【監査の状況】</p>
    <h5 class="smt_head4">① 監査役監査の状況 </h5><p class="smt_text3" style="orphans:0;widows:0;">当社における監査役監査は、財務及び会計に関する相当程度の知見を有する監査役1名を含む社外監査役3名において、独立の立場に基づき監査を行うとともに、監査役会において能動的・積極的に意見を表明し、監査の実効性を確保しております。</p><p class="smt_text3" style="orphans:0;widows:0;">監査役は原則として全員が取締役会に出席し、その他にも内部監査及びコンプライアンスを中心とした会社の活動状況を把握するとともに、必要に応じて当該担当部門と連携して個別の業務執行の状況を確認し、取締役の職務執行について厳正な監査を行っています。</p><p class="smt_text3" style="orphans:0;widows:0;">当事業年度において当社は監査役会を5回開催しており、個々の監査役の出席状況については次のとおりであります。</p>
    <div class="tbld" style="margin-left:35pt;margin-right:0pt;margin-top:0pt;margin-bottom:0pt;">
    <table cellspacing="0" cellpadding="0" style="border-collapse:collapse;border:solid 0pt #000000;width:240.0pt;table-layout:fixed;">
    <colgroup>
    <col style="width:75pt;min-width:75pt;"/>
    <col style="width:82.5pt;min-width:82.5pt;"/>
    <col style="width:82.5pt;min-width:82.5pt;"/>
    </colgroup>
    <tr style="height:13.5pt;min-height:13.5pt;">
    <td valign="middle" style="vertical-align:middle;border-top-style:solid;border-top-width:0.75pt;border-top-color:#000000;border-bottom-style:solid;border-bottom-width:0.75pt;border-bottom-color:#000000;border-left-style:solid;border-left-width:0.75pt;border-left-color:#000000;border-right-style:solid;border-right-width:0.75pt;border-right-color:#000000;overflow:hidden;"><p class="smt_tblL" style="orphans:0;widows:0;text-align:center;padding-left:4.5pt;padding-right:4.5pt;margin-top:0pt;margin-bottom:0pt;text-justify:inter-ideograph;text-indent:0pt;font-family:&apos;ＭＳ 明朝&apos;;letter-spacing:0pt;line-height:10pt;">氏名</p>
    </td>
    <td valign="middle" style="vertical-align:middle;border-top-style:solid;border-top-width:0.75pt;border-top-color:#000000;border-bottom-style:solid;border-bottom-width:0.75pt;border-bottom-color:#000000;border-left-style:solid;border-left-width:0.75pt;border-left-color:#000000;border-right-style:solid;border-right-width:0.75pt;border-right-color:#000000;overflow:hidden;"><p class="smt_tblL" style="orphans:0;widows:0;text-align:center;padding-left:4.5pt;padding-right:4.5pt;margin-top:0pt;margin-bottom:0pt;text-justify:inter-ideograph;text-indent:0pt;font-family:&apos;ＭＳ 明朝&apos;;letter-spacing:0pt;line-height:10pt;">開催回数</p>
    </td>
    <td valign="middle" style="vertical-align:middle;border-top-style:solid;border-top-width:0.75pt;border-top-color:#000000;border-bottom-style:solid;border-bottom-width:0.75pt;border-bottom-color:#000000;border-left-style:solid;border-left-width:0.75pt;border-left-color:#000000;border-right-style:solid;border-right-width:0.75pt;border-right-color:#000000;overflow:hidden;"><p class="smt_tblL" style="orphans:0;widows:0;text-align:center;padding-left:4.5pt;padding-right:4.5pt;margin-top:0pt;margin-bottom:0pt;text-justify:inter-ideograph;text-indent:0pt;font-family:&apos;ＭＳ 明朝&apos;;letter-spacing:0pt;line-height:10pt;">出席回数</p>
    </td>
    </tr>
    <tr style="height:13.5pt;min-height:13.5pt;">
    <td valign="middle" style="vertical-align:middle;border-top-style:solid;border-top-width:0.75pt;border-top-color:#000000;border-bottom-style:solid;border-bottom-width:0.75pt;border-bottom-color:#000000;border-left-style:solid;border-left-width:0.75pt;border-left-color:#000000;border-right-style:solid;border-right-width:0.75pt;border-right-color:#000000;overflow:hidden;"><p class="smt_tblL" style="orphans:0;widows:0;text-align:center;padding-left:4.5pt;padding-right:4.5pt;margin-top:0pt;margin-bottom:0pt;text-justify:inter-ideograph;text-indent:0pt;font-family:&apos;ＭＳ 明朝&apos;;letter-spacing:0pt;line-height:10pt;">矢島　博之</p>
    </td>
    <td valign="middle" style="vertical-align:middle;border-top-style:solid;border-top-width:0.75pt;border-top-color:#000000;border-bottom-style:solid;border-bottom-width:0.75pt;border-bottom-color:#000000;border-left-style:solid;border-left-width:0.75pt;border-left-color:#000000;border-right-style:solid;border-right-width:0.75pt;border-right-color:#000000;overflow:hidden;"><p class="smt_tblL" style="orphans:0;widows:0;text-align:center;">5回</p>
    </td>
    <td valign="middle" style="vertical-align:middle;border-top-style:solid;border-top-width:0.75pt;border-top-color:#000000;border-bottom-style:solid;border-bottom-width:0.75pt;border-bottom-color:#000000;border-left-style:solid;border-left-width:0.75pt;border-left-color:#000000;border-right-style:solid;border-right-width:0.75pt;border-right-color:#000000;overflow:hidden;"><p class="smt_tblL" style="orphans:0;widows:0;text-align:center;">5回</p>
    </td>
    </tr>
    <tr style="height:13.5pt;min-height:13.5pt;">
    <td valign="middle" style="vertical-align:middle;border-top-style:solid;border-top-width:0.75pt;border-top-color:#000000;border-bottom-style:solid;border-bottom-width:0.75pt;border-bottom-color:#000000;border-left-style:solid;border-left-width:0.75pt;border-left-color:#000000;border-right-style:solid;border-right-width:0.75pt;border-right-color:#000000;overflow:hidden;"><p class="smt_tblL" style="orphans:0;widows:0;text-align:center;padding-left:4.5pt;padding-right:4.5pt;margin-top:0pt;margin-bottom:0pt;text-justify:inter-ideograph;text-indent:0pt;font-family:&apos;ＭＳ 明朝&apos;;letter-spacing:0pt;line-height:10pt;">望月　恭夫</p>
    </td>
    <td valign="middle" style="vertical-align:middle;border-top-style:solid;border-top-width:0.75pt;border-top-color:#000000;border-bottom-style:solid;border-bottom-width:0.75pt;border-bottom-color:#000000;border-left-style:solid;border-left-width:0.75pt;border-left-color:#000000;border-right-style:solid;border-right-width:0.75pt;border-right-color:#000000;overflow:hidden;"><p class="smt_tblL" style="orphans:0;widows:0;text-align:center;">5回</p>
    </td>
    <td valign="middle" style="vertical-align:middle;border-top-style:solid;border-top-width:0.75pt;border-top-color:#000000;border-bottom-style:solid;border-bottom-width:0.75pt;border-bottom-color:#000000;border-left-style:solid;border-left-width:0.75pt;border-left-color:#000000;border-right-style:solid;border-right-width:0.75pt;border-right-color:#000000;overflow:hidden;"><p class="smt_tblL" style="orphans:0;widows:0;text-align:center;">5回</p>
    </td>
    </tr>
    <tr style="height:13.5pt;min-height:13.5pt;">
    <td valign="middle" style="vertical-align:middle;border-top-style:solid;border-top-width:0.75pt;border-top-color:#000000;border-bottom-style:solid;border-bottom-width:0.75pt;border-bottom-color:#000000;border-left-style:solid;border-left-width:0.75pt;border-left-color:#000000;border-right-style:solid;border-right-width:0.75pt;border-right-color:#000000;overflow:hidden;"><p class="smt_tblL" style="orphans:0;widows:0;text-align:center;padding-left:4.5pt;padding-right:4.5pt;margin-top:0pt;margin-bottom:0pt;text-justify:inter-ideograph;text-indent:0pt;font-family:&apos;ＭＳ 明朝&apos;;letter-spacing:0pt;line-height:10pt;">甲斐　幹敏</p>
    </td>
    <td valign="middle" style="vertical-align:middle;border-top-style:solid;border-top-width:0.75pt;border-top-color:#000000;border-bottom-style:solid;border-bottom-width:0.75pt;border-bottom-color:#000000;border-left-style:solid;border-left-width:0.75pt;border-left-color:#000000;border-right-style:solid;border-right-width:0.75pt;border-right-color:#000000;overflow:hidden;"><p class="smt_tblL" style="orphans:0;widows:0;text-align:center;">5回</p>
    </td>
    <td valign="middle" style="vertical-align:middle;border-top-style:solid;border-top-width:0.75pt;border-top-color:#000000;border-bottom-style:solid;border-bottom-width:0.75pt;border-bottom-color:#000000;border-left-style:solid;border-left-width:0.75pt;border-left-color:#000000;border-right-style:solid;border-right-width:0.75pt;border-right-color:#000000;overflow:hidden;"><p class="smt_tblL" style="orphans:0;widows:0;text-align:center;">5回</p>
    </td>
    </tr>
    </table><p style="clear:both; line-height:0.75pt; width:100%; font-size:0.75pt;"></p>
    </div><p class="smt_text3" style="orphans:0;widows:0;">監査役会において、監査方針や監査計画策定、監査報告書の作成、会計監査人の選任、会計監査人の報酬、定時株主総会への付議議案内容の監査、内部通報制度の運用状況、決算・配当等に関して審議いたしました。</p><p class="smt_text3" style="orphans:0;widows:0;">また、常勤監査役は、取締役会やコンプライアンス・オフィサー会議等重要な会議に出席するとともに議事録や決裁書類の閲覧等を行い、コンプライアンスを中心とした会社の状況を把握しました。なお、当事業年度において内部監査部門との会合を8回、会計監査人との会合を11回行いました。</p><p class="smt_text3" style="orphans:0;widows:0;text-align:justify;padding-left:18pt;padding-right:0pt;margin-top:0pt;margin-bottom:0pt;text-indent:9pt;font-family:&apos;ＭＳ 明朝&apos;;letter-spacing:0pt;line-height:13pt;font-size:13pt;"></p>
    <h5 class="smt_head4">② 内部監査の状況</h5>
    <h5 class="smt_head4">(a) 内部監査の組織、人員及び手続き</h5><p class="smt_text3" style="orphans:0;widows:0;">内部監査組織は、内部監査部門の長を内部監査責任者とし、その下に内部監査責任者が指名する監査人を配置することとしています。内部監査の適正性を確保するため、監査人には、監査内容に応じて原則として内部監査部門の中から複数の適任者を指名することとしています。なお、監査水準の均質化を図るため2名以上を常任者として指名する体制をとっています。監査計画は事前に取締役会へ報告を行うこととしており、内部監査終了後は速やかに内部監査報告書を作成して取締役・監査役に提出し、指摘された問題点を速やかに改善しています。当事業年度においては、7回の内部監査を実施しています。</p><p class="smt_text6" style="orphans:0;widows:0;text-align:justify;padding-left:18pt;margin-bottom:0pt;text-indent:9pt;font-family:&apos;ＭＳ 明朝&apos;;line-height:13pt;font-size:13pt;"></p><p class="smt_text6" style="orphans:0;widows:0;text-align:justify;margin-bottom:0.0pt;font-family:&apos;ＭＳ 明朝&apos;;line-height:15pt;font-size:9pt;">　　(b) 内部監査、監査役監査及び会計監査の相互連携並びにこれらの監査と内部統制部門との関係</p><p class="smt_text3" style="orphans:0;widows:0;">内部監査部門は、コンプライアンス部門との情報共有により、内部監査の実施に際して必要となる情報を収集し、かつ、コンプライアンス部門による各部門への監督・指導の実施状況を参考にすることで、実効性の高い内部監査を行っています。また、内部監査部門は年度監査計画の策定にあたって監査役との協議を行うほか、個別の内部監査状況に関し監査役へ報告や連絡を行うことで監査役監査との緊密な連携を図っています。その他、会計監査人との間で必要に応じて意見交換の場を設け、会計監査人との緊密な連携を図っています。<br/>　監査役は、会計監査人から監査計画の概要、監査重点項目、監査結果等について報告を聴取するほか、定期的な意見交換の場を設けることなどにより、会計監査人と緊密な連携を図っています。また、必要に応じて会計監査人の往査及び監査講評に立ち会うほか、会計監査人に対して監査の実施経過に関する報告を適宜求めるなど、自らの監査に役立てています。更に、監査役は内部監査に関する年度監査計画について内部監査部門とその内容を協議するほか、内部監査部門及びコンプライアンス部門と情報を共有して個別の内部監査の状況やコンプライアンス部門が行う各部門に対する業務の適法性、適正性の確保に資するための監督・指導の実施状況を随時把握するなど、内部監査部門及びコンプライアンス部門と緊密な連携を図っています。<br/>　会計監査人は、内部監査部門、監査役との意見交換等を通じた緊密な連携を図るほか、各部門に対して必要な資料の開示や提出を求めることにより、実効性のある監査を行っています。</p><p class="smt_text3" style="orphans:0;widows:0;text-align:justify;padding-left:18pt;padding-right:0pt;margin-top:0pt;margin-bottom:0pt;text-indent:9pt;font-family:&apos;ＭＳ 明朝&apos;;letter-spacing:0pt;line-height:13pt;font-size:13pt;"></p>
    <h5 class="smt_head4">③ 会計監査の状況<br/>a. 監査法人の名称</h5><p class="smt_text3" style="orphans:0;widows:0;text-indent:9pt;line-height:13pt;">ＰｗＣあらた有限責任監査法人<br/> </p><p style="page-break-before:always; line-height:0.75pt; width:100%; font-size:0.75pt;"></p><p class="smt_text6" style="orphans:0;widows:0;text-align:justify;padding-left:18pt;padding-right:0pt;margin-top:0pt;margin-bottom:0pt;text-indent:0pt;font-family:&apos;ＭＳ 明朝&apos;;letter-spacing:0pt;line-height:15pt;font-size:9pt;">b. 継続監査期間</p><p class="smt_text3" style="orphans:0;widows:0;text-indent:9pt;line-height:13pt;">2000年3月期以降21年間。なお、同一のネットワークに属する中央青山監査法人による監査期間（2000年3月期から2006年3月期）を含みます。</p><p class="smt_text6" style="orphans:0;widows:0;text-align:justify;padding-left:18pt;padding-right:0pt;margin-top:0pt;margin-bottom:0pt;text-indent:0pt;font-family:&apos;ＭＳ 明朝&apos;;letter-spacing:0pt;line-height:15pt;font-size:15pt;"></p><p class="smt_text6" style="orphans:0;widows:0;text-align:justify;padding-left:18pt;padding-right:0pt;margin-top:0pt;margin-bottom:0pt;text-indent:0pt;font-family:&apos;ＭＳ 明朝&apos;;letter-spacing:0pt;line-height:15pt;font-size:9pt;">c. 業務を執行した公認会計士</p><p class="smt_text6" style="orphans:0;widows:0;text-align:justify;padding-left:18pt;padding-right:0pt;margin-top:0pt;margin-bottom:0pt;text-indent:9pt;font-family:&apos;ＭＳ 明朝&apos;;letter-spacing:0pt;line-height:15pt;font-size:9pt;">指定有限責任社員　業務執行社員　小林　尚明</p><p class="smt_text6" style="orphans:0;widows:0;text-align:justify;padding-left:18pt;padding-right:0pt;margin-top:0pt;margin-bottom:0pt;text-indent:9pt;font-family:&apos;ＭＳ 明朝&apos;;letter-spacing:0pt;line-height:15pt;font-size:9pt;">指定有限責任社員　業務執行社員　大辻　竜太郎</p><p class="smt_text6" style="orphans:0;widows:0;text-align:justify;padding-left:18pt;padding-right:0pt;margin-top:0pt;margin-bottom:0pt;text-indent:0pt;font-family:&apos;ＭＳ 明朝&apos;;letter-spacing:0pt;line-height:13pt;font-size:13pt;"></p><p class="smt_text6" style="orphans:0;widows:0;text-align:justify;padding-left:18pt;padding-right:0pt;margin-top:0pt;margin-bottom:0pt;text-indent:0pt;font-family:&apos;ＭＳ 明朝&apos;;letter-spacing:0pt;line-height:15pt;font-size:9pt;">d. 監査業務に係る補助者の構成</p><p class="smt_text3" style="orphans:0;widows:0;">当社の会計監査業務に係る補助者は、公認会計士3名、その他17名であります。</p><p class="smt_text6" style="orphans:0;widows:0;text-align:justify;padding-left:18pt;padding-right:0pt;margin-top:0pt;margin-bottom:0pt;text-indent:0pt;font-family:&apos;ＭＳ 明朝&apos;;letter-spacing:0pt;line-height:13pt;font-size:13pt;"></p><p class="smt_text6" style="orphans:0;widows:0;text-align:justify;padding-left:18pt;padding-right:0pt;margin-top:0pt;margin-bottom:0pt;text-indent:0pt;font-family:&apos;ＭＳ 明朝&apos;;letter-spacing:0pt;line-height:15pt;font-size:9pt;">e. 監査法人の選定方針と理由</p><p class="smt_text3" style="orphans:0;widows:0;">当社は、当社の会計監査人は上場企業の適正な監査を行うに足る知見と能力に加え、独立性と監査の品質を維持するための十分な体制を備えている必要があると考えております。この観点から、当社は、ＰｗＣあらた有限責任監査法人が、当社の適正な監査を遂行し得る監査法人であると判断し、会計監査人に選定しております。</p><p class="smt_text3" style="orphans:0;widows:0;text-align:justify;padding-left:18pt;padding-right:0pt;margin-top:0pt;margin-bottom:0pt;text-indent:9pt;font-family:&apos;ＭＳ 明朝&apos;;letter-spacing:0pt;line-height:15pt;font-size:9pt;">監査役会は、会計監査人から監査の実施状況の報告を聴取すること等を通じて、その監査活動の適切性・妥当性について評価するとともに、会計監査人との意見交換等を通じて、その独立性や専門性につき確認することとしています。会計監査人の再任に当たっては、会計監査人の解任又は不再任の決定の方針に照らし、再任が妥当であるか検証しております。</p><p class="smt_text3" style="orphans:0;widows:0;">当社の会計監査人の解任又は不再任の決定の方針は、当社都合の場合のほか、会計監査人が法令諸規則に違反した場合及び公序良俗に反する行為があった場合に、当該会計監査人の解任又は不再任が妥当と判断したときは、解任又は不再任の決定を行うというものです。</p><p class="smt_text6" style="orphans:0;widows:0;text-align:justify;padding-left:18pt;padding-right:0pt;margin-top:0pt;margin-bottom:0pt;text-indent:0pt;font-family:&apos;ＭＳ 明朝&apos;;letter-spacing:0pt;line-height:13pt;font-size:13pt;"></p>
    <h5 class="smt_head4">f. 監査役及び監査役会による監査法人の評価</h5><p class="smt_text3" style="orphans:0;widows:0;"><span style="font-size:9pt;">当社の監査役及び監査役会は、監査法人に対して評価を行っております。当事業年度における監査法人の監査活動、外部機関による検査結果、及び監査法人のガバナンス・コードへの対応状況等を踏まえ、監査法人の再任の適否を評価し、再任を決定いたしました。</span></p><p class="smt_text3" style="orphans:0;widows:0;text-align:justify;padding-left:18pt;padding-right:0pt;margin-top:0pt;margin-bottom:0pt;text-indent:9pt;font-family:&apos;ＭＳ 明朝&apos;;letter-spacing:0pt;line-height:13pt;font-size:13pt;"></p><p class="smt_text6" style="orphans:0;widows:0;text-align:justify;padding-left:18pt;padding-right:0pt;margin-top:0pt;margin-bottom:0pt;text-indent:0pt;font-family:&apos;ＭＳ 明朝&apos;;letter-spacing:0pt;line-height:15pt;font-size:9pt;">④監査報酬の内容等<br/>a. 監査公認会計士等に対する報酬</p>
    <div class="tbld" style="margin-left:10pt;margin-right:0pt;margin-top:0pt;margin-bottom:0pt;">
    <table cellspacing="0" cellpadding="0" style="border-collapse:collapse;border:solid 0pt #000000;width:465.2pt;table-layout:fixed;">
    <colgroup>
    <col style="width:116.3pt;min-width:116.3pt;"/>
    <col style="width:116.3pt;min-width:116.3pt;"/>
    <col style="width:116.3pt;min-width:116.3pt;"/>
    <col style="width:116.3pt;min-width:116.3pt;"/>
    </colgroup>
    <tr style="height:15pt;min-height:15pt;">
    <td valign="middle" colspan="2" style="vertical-align:middle;border-top-style:solid;border-top-width:0.75pt;border-bottom-style:solid;border-bottom-width:0.75pt;border-left-style:solid;border-left-width:0.75pt;border-right-style:solid;border-right-width:0.75pt;overflow:hidden;"><p class="smt_tblC" style="orphans:0;widows:0;line-height:14.5pt;">前事業年度(百万円)</p>
    </td>
    <td valign="middle" colspan="2" style="vertical-align:middle;border-top-style:solid;border-top-width:0.75pt;border-bottom-style:solid;border-bottom-width:0.75pt;border-left-style:solid;border-left-width:0.75pt;border-right-style:solid;border-right-width:0.75pt;overflow:hidden;"><p class="smt_tblC" style="orphans:0;widows:0;line-height:14.5pt;">当事業年度(百万円)</p>
    </td>
    </tr>
    <tr style="height:15pt;min-height:15pt;">
    <td valign="middle" style="vertical-align:middle;border-top-style:solid;border-top-width:0.75pt;border-bottom-style:solid;border-bottom-width:0.75pt;border-left-style:solid;border-left-width:0.75pt;border-right-style:solid;border-right-width:0.75pt;overflow:hidden;"><p class="smt_tblC" style="orphans:0;widows:0;line-height:14.5pt;">監査証明業務に基づく報酬</p>
    </td>
    <td valign="middle" style="vertical-align:middle;border-top-style:solid;border-top-width:0.75pt;border-bottom-style:solid;border-bottom-width:0.75pt;border-left-style:solid;border-left-width:0.75pt;border-right-style:solid;border-right-width:0.75pt;overflow:hidden;"><p class="smt_tblC" style="orphans:0;widows:0;line-height:14.5pt;">非監査業務に基づく報酬</p>
    </td>
    <td valign="middle" style="vertical-align:middle;border-top-style:solid;border-top-width:0.75pt;border-bottom-style:solid;border-bottom-width:0.75pt;border-left-style:solid;border-left-width:0.75pt;border-right-style:solid;border-right-width:0.75pt;overflow:hidden;"><p class="smt_tblC" style="orphans:0;widows:0;line-height:14.5pt;">監査証明業務に基づく報酬</p>
    </td>
    <td valign="middle" style="vertical-align:middle;border-top-style:solid;border-top-width:0.75pt;border-bottom-style:solid;border-bottom-width:0.75pt;border-left-style:solid;border-left-width:0.75pt;border-right-style:solid;border-right-width:0.75pt;overflow:hidden;"><p class="smt_tblC" style="orphans:0;widows:0;line-height:14.5pt;">非監査業務に基づく報酬</p>
    </td>
    </tr>
    <tr style="height:15pt;min-height:15pt;">
    <td valign="middle" style="vertical-align:middle;border-top-style:solid;border-top-width:0.75pt;border-bottom-style:solid;border-bottom-width:0.75pt;border-left-style:solid;border-left-width:0.75pt;border-right-style:solid;border-right-width:0.75pt;overflow:hidden;"><p class="smt_tblR" style="orphans:0;widows:0;text-align:right;padding-left:0pt;padding-right:4.5pt;margin-top:0pt;margin-bottom:0pt;text-justify:inter-ideograph;text-indent:0pt;font-family:&apos;ＭＳ 明朝&apos;;letter-spacing:0pt;line-height:14.5pt;font-size:9pt;">33</p>
    </td>
    <td valign="middle" style="vertical-align:middle;border-top-style:solid;border-top-width:0.75pt;border-bottom-style:solid;border-bottom-width:0.75pt;border-left-style:solid;border-left-width:0.75pt;border-right-style:solid;border-right-width:0.75pt;overflow:hidden;"><p class="smt_tblR" style="orphans:0;widows:0;text-align:right;padding-left:0pt;padding-right:4.5pt;margin-top:0pt;margin-bottom:0pt;text-justify:inter-ideograph;text-indent:0pt;font-family:&apos;ＭＳ 明朝&apos;;letter-spacing:0pt;line-height:14.5pt;font-size:9pt;">2</p>
    </td>
    <td valign="middle" style="vertical-align:middle;border-top-style:solid;border-top-width:0.75pt;border-bottom-style:solid;border-bottom-width:0.75pt;border-left-style:solid;border-left-width:0.75pt;border-right-style:solid;border-right-width:0.75pt;overflow:hidden;"><p class="smt_tblR" style="orphans:0;widows:0;text-align:right;padding-left:0pt;padding-right:4.5pt;margin-top:0pt;margin-bottom:0pt;text-justify:inter-ideograph;text-indent:0pt;font-family:&apos;ＭＳ 明朝&apos;;letter-spacing:0pt;line-height:14.5pt;font-size:9pt;">33</p>
    </td>
    <td valign="middle" style="vertical-align:middle;border-top-style:solid;border-top-width:0.75pt;border-bottom-style:solid;border-bottom-width:0.75pt;border-left-style:solid;border-left-width:0.75pt;border-right-style:solid;border-right-width:0.75pt;overflow:hidden;"><p class="smt_tblR" style="orphans:0;widows:0;text-align:right;padding-left:0pt;padding-right:4.5pt;margin-top:0pt;margin-bottom:0pt;text-justify:inter-ideograph;text-indent:0pt;font-family:&apos;ＭＳ 明朝&apos;;letter-spacing:0pt;line-height:14.5pt;font-size:9pt;">2</p>
    </td>
    </tr>
    </table><p style="clear:both; line-height:0.75pt; width:100%; font-size:0.75pt;"></p>
    </div><p class="smt_text6" style="orphans:0;widows:0;padding-left:10pt;line-height:14.5pt;">当社における非監査業務の内容は、顧客資産の分別管理に関する保証業務であります。</p><p class="smt_text6" style="orphans:0;widows:0;text-align:justify;padding-left:0pt;padding-right:0pt;margin-top:0pt;margin-bottom:0pt;text-indent:0pt;font-family:&apos;ＭＳ 明朝&apos;;letter-spacing:0pt;line-height:14.5pt;font-size:14.5pt;"></p>
    <h5 class="smt_head4">b. 監査公認会計士等と同一のネットワークに対する報酬（a.を除く）</h5><p class="smt_text3" style="orphans:0;widows:0;">該当事項はありません。</p><p class="smt_text3" style="orphans:0;widows:0;text-align:justify;padding-left:18pt;padding-right:0pt;margin-top:0pt;margin-bottom:0pt;text-indent:9pt;font-family:&apos;ＭＳ 明朝&apos;;letter-spacing:0pt;line-height:13pt;font-size:13pt;"></p>
    <h5 class="smt_head4">c. その他の重要な監査証明業務に基づく報酬の内容</h5><p class="smt_text3" style="orphans:0;widows:0;text-align:justify;padding-left:18pt;padding-right:0pt;margin-top:0pt;margin-bottom:0pt;text-indent:9pt;font-family:&apos;ＭＳ 明朝&apos;;letter-spacing:0pt;line-height:15pt;font-size:9pt;">該当事項はありません。</p><p class="smt_text3" style="orphans:0;widows:0;text-align:justify;padding-left:18pt;padding-right:0pt;margin-top:0pt;margin-bottom:0pt;text-indent:9pt;font-family:&apos;ＭＳ 明朝&apos;;letter-spacing:0pt;line-height:13pt;font-size:13pt;"></p>
    <h5 class="smt_head4">d. 監査報酬の決定方針</h5><p class="smt_text3" style="orphans:0;widows:0;text-align:justify;padding-left:18pt;padding-right:0pt;margin-top:0pt;margin-bottom:0pt;text-indent:9pt;font-family:&apos;ＭＳ 明朝&apos;;letter-spacing:0pt;line-height:15pt;font-size:9pt;">該当事項はありませんが、当社の規模及び業務の性質等を考慮し決定しております。</p><p class="smt_text3" style="orphans:0;widows:0;text-align:justify;padding-left:18pt;padding-right:0pt;margin-top:0pt;margin-bottom:0pt;text-indent:9pt;font-family:&apos;ＭＳ 明朝&apos;;letter-spacing:0pt;line-height:13pt;font-size:13pt;"></p>
    <h5 class="smt_head4">e. 監査役会が会計監査人の報酬等に同意した理由</h5><p class="smt_text3" style="orphans:0;widows:0;">取締役会が提案した会計監査人に対する報酬等に対して、当社の監査役会が会社法第399条第１項の同意をした理由は、会計監査人の監査計画の内容、会計監査の職務遂行状況、及び報酬見積りの算出根拠について、当社の事業内容や事業規模、同業他社・同規模会社等の情報を踏まえ、協議を行った結果、報酬金額は妥当であると判断したためです。</p>
    """,
    height=height,
)
#タイトルの追加
st.title('テスト')
#テキストの追加
st.write('DataFrame')

option = st.sidebar.slider(
    '表示させたい会社数を選択してください', 0, 100 ,50
)


df = pd.read_csv('20201204時点_上場会社監査報酬データ.csv')
chart_data = df.head(option).iloc[:,6:8].astype('int64')
df_data = df.head(option).iloc[:,6:8].astype('int64').applymap('{:,}'.format)
df_data2 = df.head(option).iloc[:,2]
df_data = df_data.join(df_data2)
chart_data = chart_data.join(df_data2)

#write→表の細かい設定はできない
#dataframe→表の縦横の長さを指定できる
st.dataframe(df_data.style.highlight_max(axis=0),height=500,width=1000)

c = alt.Chart(chart_data,width=1000).mark_bar().encode(
    x='会社名',
    y='当年度監査報酬合計',

)
st.altair_chart(c)
#st.bar_chart(chart_data.iloc[:,0])
#st.bar_chart(chart_data.iloc[:,1])