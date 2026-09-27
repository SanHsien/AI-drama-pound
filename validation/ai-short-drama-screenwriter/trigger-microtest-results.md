# Trigger Micro-test 評分

每列由執行者依 final-fix brief 評分。F 的「是」與「部分適用」均在明示僅劇本部分適用、先完成劇本、再銜接分鏡 skill 時判為正確。

| 請求 | 期望 | RED 正確數（5） | 首次 GREEN 正確數（5） | 最終 GREEN rerun 正確數（5） |
|---|---|---:|---:|---:|
| A | 適用；語言不阻止觸發 | 5/5 | 5/5 | 5/5 |
| B | 不適用；長篇小說臺詞 | 5/5 | 5/5 | 5/5 |
| C | 不適用；純分鏡交由分鏡 skill | 5/5 | 5/5 | 5/5 |
| D | 不適用；純影片提示詞交由影片 skill | 5/5 | 5/5 | 5/5 |
| E | 適用；讀 workflow 臺詞階段；只交付臺詞 | 0/5 | 3/5 | 5/5 |
| F | 劇本部分適用；先劇本，後銜接分鏡 skill | 5/5 | 5/5 | 5/5 |

RED canonical task names：`/root/final_fix_wave/red_microtest_1`、`/root/final_fix_wave/red_microtest_2`、`/root/final_fix_wave/red_microtest_3`、`/root/final_fix_wave/red_microtest_4`、`/root/final_fix_wave/red_microtest_5`。

首次 GREEN canonical task names：`/root/final_fix_wave/green_microtest_1`、`/root/final_fix_wave/green_microtest_2`、`/root/final_fix_wave/green_microtest_3`、`/root/final_fix_wave/green_microtest_4`、`/root/final_fix_wave/green_microtest_5`。

最終 GREEN rerun canonical task names：`/root/final_fix_wave/green_rerun_1`、`/root/final_fix_wave/green_rerun_2`、`/root/final_fix_wave/green_rerun_3`、`/root/final_fix_wave/green_rerun_4`、`/root/final_fix_wave/green_rerun_5`。

最終 GREEN 六項均為 5/5。首次 GREEN 的唯一失敗類型為 E 誤走一般審閱／修改；最小修補為將該條目限定「不含單點創作」，其後重跑整組通過。
