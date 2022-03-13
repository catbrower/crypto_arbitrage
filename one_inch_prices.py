import json
import cloudscraper

def get_decimals(token):
    if token == "USDT" or token == "USDC":
        return 6
    elif token == 'XAMP':
        return 9
    else:
        return 18

def get_quote_url(token0, token1):
    base_url = 'https://pathfinder.1inch.io/v1.2/chain/1/router/v4/quotes'
    url_parts = [
        ['deepLevel', 2],
        ['mainRouteParts', 10],
        ['parts', 50],
        ['virtualParts', 50],
        ['walletAddress', "null"],
        ['fromTokenAddress', token0],
        ['toTokenAddress', token1],
        ['amount', 10 ** 18],
        ['gasPrice', 34169050719],
        ['protocolWhiteList', "WETH,UNISWAP_V1,UNISWAP_V2,SUSHI,MOONISWAP,BALANCER,COMPOUND,CURVE,CURVE_V2_SPELL_2_ASSET,CURVE_V2_THRESHOLDNETWORK_2_ASSET,CHAI,OASIS,KYBER,AAVE,IEARN,BANCOR,PMM1,CREAMSWAP,SWERVE,BLACKHOLESWAP,DODO,DODO_V2,VALUELIQUID,SHELL,DEFISWAP,COFIX,SAKESWAP,LUASWAP,MINISWAP,MSTABLE,PMM2,AAVE_LIQUIDATOR,SYNTHETIX,AAVE_V2,ST_ETH,ONE_INCH_LP,ONE_INCH_LP_1_1,ONE_INCH_LP_MIGRATOR,ONE_INCH_LP_MIGRATOR_V1_1,UNISWAP_V2_MIGRATOR,SUSHISWAP_MIGRATOR,LINKSWAP,S_FINANCE,PSM,POWERINDEX,INDEXED_FINANCE,PMM3,XSIGMA,CREAM_LENDING,SMOOTHY_FINANCE,SADDLE,PMM4,KYBER_DMM,BALANCER_V2,UNISWAP_V3,SETH_WRAPPER,CURVE_V2,CURVE_V2_EURS_2_ASSET,CURVE_V2_EURT_2_ASSET,CURVE_V2_XAUT_2_ASSET,CURVE_V2_ETH_CRV,CURVE_V2_ETH_CVX,CONVERGENCE_X,ONE_INCH_LIMIT_ORDER,ONE_INCH_LIMIT_ORDER_V2,DFX_FINANCE,FIXED_FEE_SWAP,DXSWAP,CLIPPER,SHIBASWAP,UNIFI,PMMX,PMM5,PSM_PAX,PMM2MM,PMM2MM1,WSTETH,DEFI_PLAZA,FIXED_FEE_SWAP_V3,SYNTHETIX_WRAPPER,SYNAPSE,CURVE_V2_YFI_2_ASSET&protocols=UNISWAP_V1,UNISWAP_V2,SUSHI,BALANCER,CURVE,CURVE_V2_SPELL_2_ASSET,CURVE_V2_THRESHOLDNETWORK_2_ASSET,CHAI,OASIS,KYBER,BANCOR,CREAMSWAP,SWERVE,DODO,DODO_V2,VALUELIQUID,SHELL,DEFISWAP,COFIX,SAKESWAP,LUASWAP,MINISWAP,MSTABLE,ONE_INCH_LP_MIGRATOR_V1_1,LINKSWAP,S_FINANCE,POWERINDEX,INDEXED_FINANCE,XSIGMA,SMOOTHY_FINANCE,SADDLE,KYBER_DMM,BALANCER_V2,UNISWAP_V3,SETH_WRAPPER,CURVE_V2,CURVE_V2_EURS_2_ASSET,CURVE_V2_EURT_2_ASSET,CURVE_V2_XAUT_2_ASSET,CURVE_V2_ETH_CRV,CURVE_V2_ETH_CVX,CONVERGENCE_X,ONE_INCH_LIMIT_ORDER_V2,DFX_FINANCE,FIXED_FEE_SWAP,DXSWAP,CLIPPER,SHIBASWAP,UNIFI,PSM_PAX,WSTETH,DEFI_PLAZA,FIXED_FEE_SWAP_V3,SYNTHETIX_WRAPPER,SYNAPSE,CURVE_V2_YFI_2_ASSET"],
        ['deepLevels', "1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1"],
        ['mainRoutePartsList', "1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1"],
        ['partsList', "1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1"],
        ['virtualPartsList', "1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1"]
    ]
    
    return f'%s?%s' % (base_url, '&'.join([f'%s=%s' % (x[0], x[1]) for x in url_parts]))

addresses = json.loads(open('addresses.json', 'r').read())
scraper = cloudscraper.create_scraper()

token0 = 'ETH'
token1 = 'USDT'

for to_token in addresses['tokens'].keys():
    if to_token == 'ETH':
        continue

    url = get_quote_url(addresses['tokens'][token0], addresses['tokens'][to_token])
    res = json.loads(scraper.get(url).text)
    print(f'%s:\t%s' % (to_token, int(res['bestResult']['toTokenAmount']) / (10 ** get_decimals(to_token))))