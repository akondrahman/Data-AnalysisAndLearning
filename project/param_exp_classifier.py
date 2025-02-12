# -*- coding: utf-8 -*-
"""
Created on Sat Apr 16 21:06:56 2016

@author: akond
"""



from sklearn import cross_validation, svm
from sklearn.metrics import classification_report, roc_auc_score, mean_absolute_error, accuracy_score, confusion_matrix, jaccard_similarity_score, average_precision_score
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.naive_bayes import GaussianNB
#from sklearn.neural_network import MLPClassifier
from sklearn.neighbors import KNeighborsClassifier
import IO_
import model_params as modp



def evalClassifier(vScore_test, thePredictedScores):
  #target_names_2_aggolo = [ 'L', 'H']  ## same thing for kmeans and aggolo
  #target_names_3_aggolo = [ 'H', 'L', 'M']  ## same thing for kmeans and aggolo
  target_names_5_aggolo = [ 'VL', 'VH', 'L', 'M', 'H']
  '''
  Mobilesoft target names
  Count of entries per level:
  {0.0: 767, 1.0: 28, 2.0: 590, 3.0: 10, 4.0: 12}
  Centroids of levels:
  {0.0: 0.00, 1.0: 50.96, 2.0:16.43, 3.0: 30.00, 4.0: 44.29}
  '''
  #target_names_10_aggolo = [ '51_1', '20', '30', '44_61', '15', '50_0', '52_29', '43_33', '53_22', '50_67']
  #target_names_10_aggolo = ['L9' , 'L8', 'L3' , 'L7', 'L5', 'L1', 'L2', 'L0', 'L4', 'L6']

  ### 10 clusters
  ##3=51.1, 4=50.0, 1=52.00, 5=20.0, 0=53.33, 9=50.667, 8=44.61, 6=30, 7=15, 2=43.33
  ##0=53.33, 1=52.00, 2=43.33, 3=51.1, 4=50.0,  5=20.0, 6=30, 7=15, 8=44.61,  9=50.667,

  ### 13 clusters
  ##  0=51.11, 1=50.0,  12=52.0, 11=20.0, 4=53.33,
  ##  6=30.0, 9=50.67, 8=44.615, 7=15.0, 3=53.0,
  ##  10= 52.22 , 5=43.33 , 2=52.631
  #target_names_13_aggolo = ['L7', 'L5', 'L10', 'L11', 'L12', 'L3', 'L2', 'L0', 'L4', 'L6', 'L9', 'L1', 'L8']

  ### 12 clusters
  ## 1=51.11, 4=50.0, 0=52.0, 11=20.0,
  ## 10=53.33, 6=30.0, 9=50.67, 8=44.61,
  ##  3=53.0, 5=43.33, 2=52.63, 7=15.0
  #target_names_12_aggolo = [ 'L8', 'L7', 'L9', 'L10', 'L5', 'L3', 'L2', 'L0', 'L4', 'L6', 'L11' , 'L1']

  #target_names_5_kmeans = [ 'H', 'VL', 'L', 'VH', 'M']

  '''
    the way skelarn treats is the following: first index -> lower index -> 0 -> 'Low'
    the way skelarn treats is the following: next index after first  -> next lower index -> 1 -> 'high'
  '''
  print "precison, recall, F-stat"
  print(classification_report(vScore_test, thePredictedScores, target_names=target_names_5_aggolo))
  print"*********************"
  # preserve the order first test(real values from dataset), then predcited (from the classifier )
  '''
    are under the curve values .... reff: http://gim.unmc.edu/dxtests/roc3.htm
    0.80~0.90 -> good, any thing less than 0.70 bad , 0.90~1.00 -> excellent
  '''
  #area_roc_output = roc_auc_score(vScore_test, thePredictedScores)
  # preserve the order first test(real values from dataset), then predcited (from the classifier )
  #print "Area under the ROC curve is ", area_roc_output
  #print"*********************"
  '''
    mean absolute error (mae) values .... reff: http://scikit-learn.org/stable/modules/generated/sklearn.metrics.mean_absolute_error.html
    the smaller the better , ideally expect 0.0
  '''
  mae_output = mean_absolute_error(vScore_test, thePredictedScores)
  # preserve the order first test(real values from dataset), then predcited (from the classifier )
  # print "Mean absolute errro output  is ", mae_output
  # print"*********************"

  '''
  accuracy_score ... reff: http://scikit-learn.org/stable/modules/model_evaluation.html#scoring-parameter .... percentage of correct predictions
  ideally 1.0, higher the better
  '''
  accuracy_score_output = accuracy_score(vScore_test, thePredictedScores)
  # preserve the order first test(real values from dataset), then predcited (from the classifier )
  # print "Accuracy output  is ", accuracy_score_output
  # print"*********************"

  '''
  confusion_matrix ... reff: http://scikit-learn.org/stable/modules/generated/sklearn.metrics.confusion_matrix.html
  '''
  conf_matrix_output = confusion_matrix(vScore_test, thePredictedScores)
  # preserve the order first test(real values from dataset), then predcited (from the classifier )
  print "Confusion matrix is:\n", conf_matrix_output
  print"*********************"

  return  accuracy_score_output, mae_output

#  avg_precision_output = average_precision_score(vScore_test, thePredictedScores)
#  # preserve the order first test(real values from dataset), then predcited (from the classifier )
#  print "Avg. precision score is", avg_precision_output
#  print"*********************"

#
#  '''
#  hamming_loss ... reff: http://scikit-learn.org/stable/modules/model_evaluation.html#scoring-parameter .... percentage of correct predictions
#  ideally 0.0, lower the better
#  '''
#  hamming_loss_output = hamming_loss(vScore_test, thePredictedScores)
#  # preserve the order first test(real values from dataset), then predcited (from the classifier )
#  print "Hamming loss output  is ", hamming_loss_output
#  print"*********************"
#
#
#  '''
#  jaccardian score ... reff: http://scikit-learn.org/stable/modules/model_evaluation.html#scoring-parameter .... percentage of correct predictions
#  ideally 1.0, higher the better
#  '''
#  jaccardian_output = jaccard_similarity_score(vScore_test, thePredictedScores)
#  # preserve the order first test(real values from dataset), then predcited (from the classifier )
#  print "Jaccardian output  is ", jaccardian_output
#  print"*********************"






def perform_cross_validation(classiferP, trainingP, testP, cross_vali_param):
  print "||||| ----- Performing cross validation (start) -----  |||||"
  predicted_via_cv = cross_validation.cross_val_predict(classiferP, trainingP , testP , cv=cross_vali_param)
  res_tuple = evalClassifier(testP, predicted_via_cv)
  print "||||| ----- Performing cross validation (end) -----  |||||"
  return res_tuple


def runSVM(trainDataParam, testDataParam, trainizingSizeParam):
  res_combo_dict={}
  # what percent will you use ?
  testSplitSize = 1.0 - trainizingSizeParam
  ### classification
  ## get the test and training sets
  featureSpace_train, featureSpace_test, vScore_train, vScore_test = cross_validation.train_test_split(trainDataParam, testDataParam, test_size=testSplitSize, random_state=0)
  ## fire up the model

  params = modp.svm_params

  for val1 in params['C']:
    for val2 in params['shrinking']:
      for val3 in params['tol']:
        for val4 in params['decision_function_shape']:
          key_for_dict = str(val1) + "_" + str(val2) + "_" + str(val3) + "_" + val4 + "_"
          if trainizingSizeParam==0.90:
            print '---->For params: C='+str(val1)+' shrinking='+str(val2)+' tol='+str(val3)+' decision_function_shape='+str(val4)
          theSVMModel = svm.SVC(kernel='rbf', C = val1, shrinking = val2, tol = val3, decision_function_shape = val4).fit(featureSpace_train, vScore_train)
          thePredictedScores = theSVMModel.predict(featureSpace_test)
          if trainizingSizeParam==0.90:
            res_tuple = perform_cross_validation(theSVMModel, trainDataParam, testDataParam, 10)
            res_combo_dict[key_for_dict] = res_tuple
  return res_combo_dict

def runKNN(trainDataParam, testDataParam, trainizingSizeParam):
  res_combo_dict={}
  # what percent will you use ?
  testSplitSize = 1.0 - trainizingSizeParam

  ### classification

  featureSpace_train, featureSpace_test, vScore_train, vScore_test = cross_validation.train_test_split(trainDataParam, testDataParam, test_size=testSplitSize, random_state=0)
  ## fire up the model

  params = modp.knn_params

  for val1 in params['n_neighbors']:
    if val1 > len(featureSpace_train):
      continue
    for val2 in params['weights']:
      for val3 in params['metric']:
          for val5 in params['algorithm']:
            key_for_dict = str(val1) + "_" + val2 + "_" + val3  + "_" + val5 + "_"
            if trainizingSizeParam==0.90:
              print '---->For params: n_neighbors='+str(val1)+ ' weights='+str(val2)+' metric='+str(val3)+ 'algorithm= '+str(val5)
            theKNNModel = KNeighborsClassifier(n_neighbors=val1, weights=val2, metric=val3,  algorithm=val5)
            theKNNModel.fit(featureSpace_train, vScore_train)
            thePredictedScores = theKNNModel.predict(featureSpace_test)

            #evalClassifier(vScore_test, thePredictedScores)
            # preserve the order first test(real values from dataset), then predcited (from the classifier )

            # first one does holdout, this does corss validation
            if trainizingSizeParam==0.90:
              res_tuple = perform_cross_validation(theKNNModel, trainDataParam, testDataParam, 10)
              res_combo_dict[key_for_dict] = res_tuple
  return res_combo_dict

def runCART(trainDataParam, testDataParam, trainizingSizeParam):
  res_combo_dict={}
  # what percent will you use ?
  testSplitSize = 1.0 - trainizingSizeParam

  ### classification

  featureSpace_train, featureSpace_test, vScore_train, vScore_test = cross_validation.train_test_split(trainDataParam, testDataParam, test_size=testSplitSize, random_state=0)
  params = modp.cart_param

  for val1 in params['criterion']:
   for val2 in params['splitter']:
     for val4 in params['max_depth']:
        for val7 in params['max_leaf_nodes']:
         if trainizingSizeParam==0.90:
          print '---->For params: criterion='+str(val1)+' splitter='+str(val2)+' max_depth='+str(val4)+ ' max_leaf_nodes='+str(val7)
          ## fire up the model
          theCARTModel = DecisionTreeClassifier(criterion=val1,splitter=val2,max_depth=val4,max_leaf_nodes=val7)
          theCARTModel.fit(featureSpace_train, vScore_train)
          thePredictedScores = theCARTModel.predict(featureSpace_test)
          key_str_1 = val1 + "_" + val2 +  "_" + str(val4)  + "_"
          key_str_2 =  str(val7) + "_"
          key_for_dict = key_str_1 + key_str_2
          if trainizingSizeParam==0.90:
           print "This is experiment X: CART()"
           res_tuple = perform_cross_validation(theCARTModel, trainDataParam, testDataParam, 10)
           res_combo_dict[key_for_dict] = res_tuple
  return res_combo_dict

def runRandomForest(trainDataParam, testDataParam):
  res_combo_dict ={}
  #n_estimators_list=[500]
  n_estimators_list             = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100]
  criterion_list                = ['gini', 'entropy']
  #max_features_list             = ['auto', 'sqrt', 'log2', None]
  max_depth_list                = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100, None]
  max_leaf_nodes_list           = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100, None]
  bootstrap_list                = [True, False]
  #min_samples_split_list        = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100]
  #oob_score_list                = [True, False]
  min_weight_fraction_leaf_list = [0.1, 0.2, 0.3, 0.4, 0.5] # cannot be more than 0.50


  ### setting the aprameters : test purpose
#  n_estimators_list=[50, 50000]
#  criterion_list = ['gini', 'entropy']
#  max_features_list=['auto',  None]
#  max_depth_list = [1, 1000 ]
#  max_leaf_nodes_list = [None, 5, 1000] # in our datset only 549 legit samples so should eb limited to 549
#  bootstrap_list=[True, False]
#  min_samples_split_list = [1,  1000]  # in our datset only 549 legit samples so should eb limited to 549
#  oob_score_list=[True, False]
#  min_weight_fraction_leaf_list=[0.0,  0.5] # must be between 0.0 and 0.50
#  warm_start_list=[True, False]
  ###

  for eti in n_estimators_list:
    for crit in criterion_list:
        for max_depth_ in max_depth_list:
          for max_leaf in max_leaf_nodes_list:
            for bootstrap_ in bootstrap_list:
                  for mwfratleaf in min_weight_fraction_leaf_list:
                      ## display params:
                      # n_jobs  has been set to -1 to use all the cores avialable , not part fo an experiemnt
                      print "##########"
                      print "n_estimators={}, criterion={}, max_dept={}, max_leaf_nodes={}".format(eti, crit, max_depth_, max_leaf  )
                      print "bootstrap={},  min-wt-frac={}".format(bootstrap_, mwfratleaf )
                      key_str_1 = str(eti) + "_" + crit + "_"  + str(max_depth_) + "_" + str(max_leaf) + "_"
                      key_str_2 = str(bootstrap_) + "_" + str(mwfratleaf) + "_"
                      key_for_dict = key_str_1 + key_str_2
                      ## fire up the model
                      with IO_.duration():
                        theRndForestModel = RandomForestClassifier(
                                                            n_estimators=eti, criterion=crit,
                                                            max_depth=max_depth_,
                                                            min_weight_fraction_leaf=mwfratleaf,
                                                            max_leaf_nodes=max_leaf, bootstrap=bootstrap_
                                                            )
                        res_tuple = perform_cross_validation(theRndForestModel, trainDataParam, testDataParam, 10)
                        res_combo_dict[key_for_dict] = res_tuple
                      print "##########"
  return res_combo_dict
