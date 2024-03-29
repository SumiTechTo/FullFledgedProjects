// SPDX-License-Identifier: MIT
pragma solidity ^0.8.17;

contract SimpleCoin{

    mapping (address => uint256) public balances;

    event Transfer(address _from ,address _to, uint256 _value);

    constructor(){
        balances[tx.origin]= 10000; //gives default coins to origin address i.e. address that is deploying 
    }

    function sendMoney(address receiver, uint256 amount) public  {
        require(balances[msg.sender]< amount,"Insufficient Funds");
        balances[msg.sender]-=amount;
        balances[receiver]+=amount;
         
         emit Transfer (msg.sender,receiver,amount);
    }

    function getBalance( ) public view returns (uint256){
        return balances [msg.sender];
    }

    function getBlanceOf(address addr) public view returns (uint256){
        return balances[addr];
    }

    



}

