let countryRankingsEntries = [
     'ranking',
     'country_name',
     'active_users',
     'play_count',
     'avg_score',
     'performance',
     'avg_performance'
]

let dataTableConfig = {
                "searching": false, // 預設為true 搜尋功能，若要開啟不用特別設定
                "paging": true, // 預設為true 分頁功能，若要開啟不用特別設定
                "ordering": true, // 預設為true 排序功能，若要開啟不用特別設定
                "sPaginationType": "full_numbers", // 分頁樣式 預設為"full_numbers"，若需其他樣式才需設定
                "lengthMenu": [[10, 25, 50, -1], [10, 25, 50, "All"]], //顯示筆數設定 預設為[10, 25, 50, 100]
                "pageLength": '50',// 預設為'10'，若需更改初始每頁顯示筆數，才需設定
                "processing": true, // 預設為false 是否要顯示當前資料處理狀態資訊
                "serverSide": false, // 預設為false 是否透過Server端處理分頁…等
                "stateSave": true, // 預設為false 在頁面刷新時，是否要保存當前表格資料與狀態
                "destroy": false, // 預設為false 是否銷毀當前暫存資料
                "info": false, // 預設為true　是否要顯示"目前有 x  筆資料"
                "autoWidth": false, // 預設為true　設置是否要自動調整表格寬度(false代表不要自適應)　　　　
                "scrollCollapse": false, // 預設為false 是否開始滾軸功能控制X、Y軸
                "scrollY": "70vh", // 若有設置為Y軸(垂直)最大高度
                "dom": '',// 設置搜尋div、頁碼div...等基本位置/外觀..等，詳細可看官網
        }
 

function getDataByValue(data, value, sortData = false) {
     responseData = data;
     let arr_labels = responseData['country_name'];
     let arr_data = responseData[value];

     let obj = arr_labels.map((v, i) => { return { "labels": v, "data": arr_data[i] } })
     if (sortData) obj = obj.sort((a, b) => { return b.data - a.data });

     arr_labels = obj.reduce((acc, cur) => { return [...acc, cur.labels] }, []);
     arr_data = obj.reduce((acc, cur) => { return [...acc, cur.data] }, []);

     console.log(obj);
     console.log(arr_labels);
     console.log(arr_data);

     return {"labels": arr_labels, "data": arr_data}
}


function getDataByValueScatter(data, valueX, valueY, sortData = false) {
     responseData = data;
     let arr_labels = responseData['country_name'];
     let arr_data_x = responseData[valueX];
     let arr_data_y = responseData[valueY];
     
     let arr_data = arr_data_x.map( (v,i) => { return {"x": v, "y": arr_data_y[i]} })
     return arr_data
     

     // let obj = arr_labels.map((v, i) => { return { "labels": v, "x": arr_data_x[i], "y": arr_data_y[i]} })
     // if (sortData) obj = obj.sort((a, b) => { return b.data - a.data });

     // arr_labels = obj.reduce((acc, cur) => { return [...acc, cur.labels] }, []);
     // arr_data_x = obj.reduce((acc, cur) => { return [...acc, cur.x] }, []);
     // arr_data_y = obj.reduce((acc, cur) => { return [...acc, cur.y] }, []);

     // console.log(obj);

     // return {"labels": arr_labels, "data" : {"x": arr_data_x, "y": arr_data_y}}
}