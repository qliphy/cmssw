// Last commit: $Id: DcuDetIdMap.cc,v 1.4 2006/07/25 10:18:30 bainbrid Exp $
// Latest tag:  $Name:  $
// Location:    $Source: /cvs_server/repositories/CMSSW/CMSSW/OnlineDB/SiStripConfigDb/src/DcuDetIdMap.cc,v $

#include "OnlineDB/SiStripConfigDb/interface/SiStripConfigDb.h"

using namespace std;

// -----------------------------------------------------------------------------
// 
const SiStripConfigDb::DcuDetIdMap& SiStripConfigDb::getDcuDetIdMap() {
  edm::LogInfo(logCategory_) << "[SiStripConfigDb::getDcuDetIdMap]"
			     << " Retrieving DetId-DCU mapping...";
  string method = "SiStripConfigDb::getDcuDetIdMap";
  
  if ( !resetDcuDetIdMap_ ) { return dcuDetIdMap_; }
  
  try {
    dcuDetIdMap_ = deviceFactory(method)->getInfos(); 
    resetDcuDetIdMap_ = false;
  }
  catch (... ) {
    handleException( method );
  }
  
  stringstream ss; 
  if ( dcuDetIdMap_.empty() ) {
    ss << "[SiStripConfigDb::getDcuDetIdMap]"
       << " No DCU-DetId map found";
    if ( !usingDb_ ) { ss << " in input 'dcuinfo.xml' file " << inputDcuInfoXml_; }
    else { ss << " in database partition '" << partition_.name_ << "'"; }
    edm::LogWarning(logCategory_) << ss.str();
    //throw cms::Exception(logCategory_) << ss.str();
  } else {
    ss << "[SiStripConfigDb::getFedConnections]"
       << " Found " << dcuDetIdMap_.size() << " entries in DCU-DetId map";
    if ( !usingDb_ ) { ss << " in input 'module.xml' file " << inputDcuInfoXml_; }
    else { ss << " in database partition '" << partition_.name_ << "'"; }
    edm::LogInfo(logCategory_) << ss.str();
  }

  return dcuDetIdMap_;
}
// -----------------------------------------------------------------------------
// 
void SiStripConfigDb::setDcuDetIdMap( const SiStripConfigDb::DcuDetIdMap& dcu_detid_map ) {
  edm::LogInfo(logCategory_) << "[SiStripConfigDb::setDcuDetIdMap]"
			     << " Setting DetId-DCU mapping...";
  resetDcuDetIdMap();
  dcuDetIdMap_ = dcu_detid_map;
  resetDcuDetIdMap_ = false;
}

// -----------------------------------------------------------------------------
//
void SiStripConfigDb::resetDcuDetIdMap() {
  dcuDetIdMap_.clear(); 
  resetDcuDetIdMap_ = true;
}

// -----------------------------------------------------------------------------
// 
void SiStripConfigDb::uploadDcuDetIdMap() {
  string method = "SiStripConfigDb::uploadDcuDetIdMap";
  try {
    deviceFactory(method)->deleteHashMapTkDcuInfo();
    deviceFactory(method)->setTkDcuInfo( dcuDetIdMap_ );
    deviceFactory(method)->addAllDetId();
  }
  catch (... ) {
    string info = "Problems updating objects in TkDcuInfoFactory!";
    handleException( method, info );
  }
}
