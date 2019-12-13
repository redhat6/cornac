# Copyright 2018 The Cornac Authors. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ============================================================================
"""Example for Variational Autoencoder for Collaborative Filtering for Implicit Feedback Datasets (Citeulike)"""

import cornac
from cornac.data import Reader
from cornac.datasets import citeulike
from cornac.eval_methods import RatioSplit

data = citeulike.load_data()

ratio_split = RatioSplit(data=data, test_size=0.2, exclude_unknowns=True,
                         verbose=True, seed=123, rating_threshold=0.5)

vaecf = cornac.models.VAECF(k=10, h=20, n_epochs=100, batch_size=100, learning_rate=0.001, beta=1.0, seed=123)

rec_20 = cornac.metrics.Recall(k=20)
ndcg_20 = cornac.metrics.NDCG(k=20)
auc = cornac.metrics.AUC()

cornac.Experiment(eval_method=ratio_split,
                  models=[vaecf],
                  metrics=[rec_20, ndcg_20, auc],
                  user_based=True).run()