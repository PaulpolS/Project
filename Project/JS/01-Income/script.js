//อ้างอิง element ใน index.html
const balance = document.getElementById('balance')
const money_plus = document.getElementById('money_plus')
const money_minus = document.getElementById('money_minus')
const list = document.getElementById('list')
const form = document.getElementById('form')
const amount = document.getElementById('amount')
const text = document.getElementById('text')

const dataTransaction = [
    {id:1,text:"ค่าขนม",amount:-100},
    {id:2,text:"ค่าขนมของแมค",amount:-499},
    {id:3,text:"เงินเดือน",amount:200000},
    {id:4,text:"อาหารแมค",amount:-100},
    {id:5,text:"BTC",amount:2000000},
]

let transactions = dataTransaction

function init(){
    list.innerHTML = '' //ทำให้List เริ่มต้นเป็นค่าว่าง
    transactions.forEach(addDataToList);
    calculateMoney()
    //ให้โปรแกรมเราวนแล้วเอาค่าใส่เข้าไปเรื่อยๆ มีการตรวจค่าในarray obj
}

addDataToList=(transactions)=>{
    const symbol = transactions.amount <0 ? '-':'+'
    const status = transactions.amount <0 ? 'minus':'plus'
    // ถ้าเงินน้อยกว่า 100 ก็ให้เป็น minus
    
    const item=document.createElement('li')
    item.classList.add(status) // ใส่class เข้าไปใน List หรือ li นั่นเอง
    //จากที่เรากำหนดคลาส plus, minus ใน CSS ที่ให้แสดงสีออกมา
    resultNumberFormat = formatNumber(Math.abs(transactions.amount))
    item.innerHTML = `${transactions.text}
    <span>${symbol}${resultNumberFormat}</span>
            <button class="delete-btn" onclick="removeData(${transactions.id})" >x</button>`
    list.appendChild(item)
}

calculateMoney=()=>{
    const amount=transactions.map(transactions=>transactions.amount)
    //map เป็นตำสั่งเข้าถึงค่าค่างๆ
    //คำนวนยอดคงเหลือ
    const total = amount.reduce((result,item)=>(result+=item),0).toFixed(2);
    // toFixed คือ จำนวนทศนิยม
    //คำนวนรายรับ
    const income = amount.filter(item=>item>0).reduce((result,item)=>(result+=item),0)
    const expense = amount.filter(item=>item<0).reduce((result,item)=>(result+=item),0)*(-1)

    //แสดงผล
    balance.innerHTML = formatNumber(total)
    money_plus.innerText = formatNumber(income)
    money_minus.innerText = formatNumber(expense)
}

//เอามาจากคนอื่น ใช้ในการใส่ , เช่น 100000 => 100
function formatNumber(num) {
    return num.toString().replace(/(\d)(?=(\d{3})+(?!\d))/g, '$1,')
}

//สุ่มไอดี
function autoID(){
    return Math.floor(Math.random()*10000000)
}

//บันทึกข้อมูล
function addTransaction(e){
    e.preventDefault()
    if(text.value.trim() === '' || amount.value.trim() === ''){
        alert("กรุณาป้อนข้อมูลครับ")
    }else{
        //เมื่อป้อนครบก็จัดข้อมูลใส่เข้าไป
        const data ={
            id:autoID(),
            text:text.value,
            amount:+amount.value
        }
        transactions.push(data);
        addDataToList(data);
        calculateMoney();
        text.value=''
        amount.value = ''
    }
}

function removeData(id){
    transactions = transactions.filter(transactions=>transactions.id !==id)
    init()
}


form.addEventListener('submit',addTransaction);
init(); // อันนี้มันจะเรียกฟังชั่นที่ใช้วนตรวจค่าใน array
