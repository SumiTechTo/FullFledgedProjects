/* Autogenerated file. Do not edit manually. */
/* tslint:disable */
/* eslint-disable */
import { Signer, utils, Contract, ContractFactory, Overrides } from "ethers";
import type { Provider, TransactionRequest } from "@ethersproject/providers";
import type { PromiseOrValue } from "../common";
import type { SimpleCoin, SimpleCoinInterface } from "../SimpleCoin";

const _abi = [
  {
    inputs: [],
    stateMutability: "nonpayable",
    type: "constructor",
  },
  {
    anonymous: false,
    inputs: [
      {
        indexed: false,
        internalType: "address",
        name: "_from",
        type: "address",
      },
      {
        indexed: false,
        internalType: "address",
        name: "_to",
        type: "address",
      },
      {
        indexed: false,
        internalType: "uint256",
        name: "_value",
        type: "uint256",
      },
    ],
    name: "Transfer",
    type: "event",
  },
  {
    inputs: [
      {
        internalType: "address",
        name: "",
        type: "address",
      },
    ],
    name: "balances",
    outputs: [
      {
        internalType: "uint256",
        name: "",
        type: "uint256",
      },
    ],
    stateMutability: "view",
    type: "function",
  },
  {
    inputs: [],
    name: "getBalance",
    outputs: [
      {
        internalType: "uint256",
        name: "",
        type: "uint256",
      },
    ],
    stateMutability: "view",
    type: "function",
  },
  {
    inputs: [
      {
        internalType: "address",
        name: "addr",
        type: "address",
      },
    ],
    name: "getBlanceOf",
    outputs: [
      {
        internalType: "uint256",
        name: "",
        type: "uint256",
      },
    ],
    stateMutability: "view",
    type: "function",
  },
  {
    inputs: [
      {
        internalType: "address",
        name: "receiver",
        type: "address",
      },
      {
        internalType: "uint256",
        name: "amount",
        type: "uint256",
      },
    ],
    name: "sendMoney",
    outputs: [],
    stateMutability: "nonpayable",
    type: "function",
  },
];

const _bytecode =
  "0x608060405234801561001057600080fd5b506127106000803273ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff168152602001908152602001600020819055506105ba806100656000396000f3fe608060405234801561001057600080fd5b506004361061004c5760003560e01c806312065fe01461005157806327e235e31461006f578063496f2b881461009f578063ee4ae2c9146100cf575b600080fd5b6100596100eb565b6040516100669190610313565b60405180910390f35b61008960048036038101906100849190610391565b610131565b6040516100969190610313565b60405180910390f35b6100b960048036038101906100b49190610391565b610149565b6040516100c69190610313565b60405180910390f35b6100e960048036038101906100e491906103ea565b610191565b005b60008060003373ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff16815260200190815260200160002054905090565b60006020528060005260406000206000915090505481565b60008060008373ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff168152602001908152602001600020549050919050565b806000803373ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff1681526020019081526020016000205410610211576040517f08c379a000000000000000000000000000000000000000000000000000000000815260040161020890610487565b60405180910390fd5b806000803373ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff168152602001908152602001600020600082825461025f91906104d6565b92505081905550806000808473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff16815260200190815260200160002060008282546102b4919061050a565b925050819055507fddf252ad1be2c89b69c2b068fc378daa952ba7f163c4a11628f55a4df523b3ef3383836040516102ee9392919061054d565b60405180910390a15050565b6000819050919050565b61030d816102fa565b82525050565b60006020820190506103286000830184610304565b92915050565b600080fd5b600073ffffffffffffffffffffffffffffffffffffffff82169050919050565b600061035e82610333565b9050919050565b61036e81610353565b811461037957600080fd5b50565b60008135905061038b81610365565b92915050565b6000602082840312156103a7576103a661032e565b5b60006103b58482850161037c565b91505092915050565b6103c7816102fa565b81146103d257600080fd5b50565b6000813590506103e4816103be565b92915050565b600080604083850312156104015761040061032e565b5b600061040f8582860161037c565b9250506020610420858286016103d5565b9150509250929050565b600082825260208201905092915050565b7f496e73756666696369656e742046756e64730000000000000000000000000000600082015250565b600061047160128361042a565b915061047c8261043b565b602082019050919050565b600060208201905081810360008301526104a081610464565b9050919050565b7f4e487b7100000000000000000000000000000000000000000000000000000000600052601160045260246000fd5b60006104e1826102fa565b91506104ec836102fa565b9250828203905081811115610504576105036104a7565b5b92915050565b6000610515826102fa565b9150610520836102fa565b9250828201905080821115610538576105376104a7565b5b92915050565b61054781610353565b82525050565b6000606082019050610562600083018661053e565b61056f602083018561053e565b61057c6040830184610304565b94935050505056fea2646970667358221220b153a5429f320b8829bb9df69e2c6541b72c22626619aa0fc21f44b0ba311b2764736f6c63430008110033";

type SimpleCoinConstructorParams =
  | [signer?: Signer]
  | ConstructorParameters<typeof ContractFactory>;

const isSuperArgs = (
  xs: SimpleCoinConstructorParams
): xs is ConstructorParameters<typeof ContractFactory> => xs.length > 1;

export class SimpleCoin__factory extends ContractFactory {
  constructor(...args: SimpleCoinConstructorParams) {
    if (isSuperArgs(args)) {
      super(...args);
    } else {
      super(_abi, _bytecode, args[0]);
    }
  }

  override deploy(
    overrides?: Overrides & { from?: PromiseOrValue<string> }
  ): Promise<SimpleCoin> {
    return super.deploy(overrides || {}) as Promise<SimpleCoin>;
  }
  override getDeployTransaction(
    overrides?: Overrides & { from?: PromiseOrValue<string> }
  ): TransactionRequest {
    return super.getDeployTransaction(overrides || {});
  }
  override attach(address: string): SimpleCoin {
    return super.attach(address) as SimpleCoin;
  }
  override connect(signer: Signer): SimpleCoin__factory {
    return super.connect(signer) as SimpleCoin__factory;
  }

  static readonly bytecode = _bytecode;
  static readonly abi = _abi;
  static createInterface(): SimpleCoinInterface {
    return new utils.Interface(_abi) as SimpleCoinInterface;
  }
  static connect(
    address: string,
    signerOrProvider: Signer | Provider
  ): SimpleCoin {
    return new Contract(address, _abi, signerOrProvider) as SimpleCoin;
  }
}
