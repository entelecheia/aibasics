# 머신러닝 모델의 학습과 평가

## 머신러닝 모델 최적화의 기초

### 목표와 개요

```{image} figs/image-3-1-1.jpeg
:width: 90%
:align: center
```

- 머신러닝 모델 최적화는 모델의 예측 성능을 극대화하는 과정입니다.
- 이 과정을 통해 데이터의 패턴을 더 잘 이해하고, 실제 세계의 복잡한 문제를 해결할 수 있습니다.

### 선형 회귀 모델의 기본 개념

```{image} figs/image-3-1-2.jpeg
:width: 90%
:align: center
```

- 선형 회귀 모델은 가장 기본적인 머신러닝 모델 중 하나입니다.
- 이 모델은 데이터의 관계를 y = ax + b 형태의 직선으로 나타냅니다.
  - 여기서 y는 종속 변수, x는 독립 변수, a는 기울기, b는 y절편입니다.
- 선형 회귀는 데이터 포인트들과 가장 잘 맞는 직선을 찾는 과정입니다.

### 최소 제곱법 소개

```{image} figs/image-3-1-3.jpeg
:width: 90%
:align: center
```

- 최소 제곱법은 선형 회귀 모델에서 매개변수 a와 b를 찾는 표준 방법입니다.
- 이 방법은 데이터 포인트와 선형 모델 간의 거리(오차)의 제곱을 최소화합니다.
- 수학적으로는 오차의 제곱 합을 최소화하는 a와 b를 찾는 것을 의미합니다.

### 평균 제곱 오차(MSE) 이해

```{image} figs/image-3-1-4.jpeg
:width: 90%
:align: center
```

- 평균 제곱 오차(MSE)는 모델의 예측값과 실제값 간의 차이를 수치화하는 방법입니다.
- MSE = (1/n) Σ(actual - prediction)²
  - 여기서 n은 샘플의 수, actual은 실제값, prediction은 예측값입니다.
- MSE가 작을수록 모델의 예측 성능이 좋다고 할 수 있습니다.
- MSE는 모델의 성능을 평가하고 비교하는 데 중요한 지표로 사용됩니다.

## 비용함수와 손실함수

### 비용함수와 손실함수의 정의

```{image} figs/image-3-2-1.jpeg
:width: 90%
:align: center
```

- **정의**:
  - 손실함수(Loss Function): 개별 데이터 포인트에 대한 모델의 오차를 측정합니다.
  - 비용함수(Cost Function): 전체 데이터셋에 대한 모델의 성능을 측정합니다.
- **중요성**:
  - 이 함수들은 모델이 얼마나 잘 또는 잘못 예측하는지를 나타내며, 이를 최소화하는 것이 모델 학습의 목표입니다.

### 평균제곱오차의 역할

```{image} figs/image-3-2-2.jpeg
:width: 90%
:align: center
```

- **평균 제곱 오차(Mean Squared Error, MSE)**:
  - MSE = (1/n) Σ(actual - prediction)²
  - 여기서 Σ는 합계, n은 샘플 수, actual은 실제 값, prediction은 예측 값입니다.
- **역할**:
  - MSE는 회귀 문제에서 자주 사용되는 손실 함수입니다.
  - 모델의 예측과 실제 값 사이의 거리를 제곱하여 평균을 내, 오차의 크기를 나타냅니다.

### 오차 함수와 목적 함수의 비교

```{image} figs/image-3-2-3.jpeg
:width: 90%
:align: center
```

- **오차 함수(Error Function)**:
  - 개별 예측값과 실제값의 차이를 측정합니다.
  - 주로 손실 함수로 사용되며, 모델이 개별 데이터 포인트에서 얼마나 잘못 예측하는지를 나타냅니다.
- **목적 함수(Objective Function)**:
  - 전체 데이터셋을 기반으로 한 모델의 전반적인 성능을 측정합니다.
  - 비용 함수와 같은 의미로 사용되며, 모델의 성능 최적화를 위한 목표를 설정합니다.
- **차이점**:
  - 오차 함수는 개별 데이터 포인트에 초점을 맞추고, 목적 함수는 전체 데이터셋에 대한 성능을 고려합니다.

## 경사하강법 (Gradient Descent)

### 경사하강법의 기본 원리

```{image} figs/image-3-3-1.jpeg
:width: 90%
:align: center
```

- **기본 개념**:
  - 경사하강법은 비용 함수의 최소점을 찾기 위한 반복적인 최적화 기법입니다.
  - 기울기(gradient)를 사용하여 각 단계에서 비용 함수를 줄여나가는 방식입니다.
- **작동 원리**:
  - 현재 위치에서 비용 함수의 기울기를 계산하고, 이를 통해 비용이 감소하는 방향으로 이동합니다.
  - 학습률(learning rate)은 이동 거리를 조절하는 파라미터로, 적절한 크기 설정이 중요합니다.

### 경사하강법의 다양한 변형

```{image} figs/image-3-3-2.jpeg
:width: 90%
:align: center
```

- **SGD (Stochastic Gradient Descent)**:
  - 매 반복에서 하나의 훈련 샘플을 사용하여 기울기를 계산합니다.
  - 빠른 계산이 가능하지만, 비용 함수의 변동이 클 수 있습니다.
- **Momentum**:
  - 이전 단계의 기울기를 고려하여 관성의 개념을 도입합니다.
  - 이를 통해 더 안정적이고 빠르게 최소점에 도달할 수 있습니다.
- **AdaGrad, RMSprop, Adam**:
  - 이 방법들은 학습률을 동적으로 조절하여 더 효율적인 최적화를 달성합니다.
  - 각각의 방법은 다른 방식으로 학습률을 조정합니다.

### 경사하강법 시각화

```{image} figs/image-3-3-3.jpeg
:width: 90%
:align: center
```

- **비용함수의 모양과 경로**:
  - 비용함수의 모양은 고차원이지만, 일반적으로 2D 또는 3D로 시각화하여 경사하강법의 경로를 이해합니다.
  - 시각화는 비용함수의 기울기와 학습률이 경로에 어떤 영향을 미치는지 보여줍니다.
- **시각적 이해**:
  - 경사하강법의 진행 과정을 그래픽으로 나타내어 비용 함수의 최소점에 도달하는 과정을 시각적으로 이해합니다.

## 머신러닝 모델의 일반화

### 과대적합과 과소적합

```{image} figs/image-3-4-1.jpeg
:width: 90%
:align: center
```

- **과대적합(Overfitting)**:
  - 모델이 학습 데이터에 너무 적합되어 새로운 데이터에 대한 예측 성능이 떨어지는 현상.
  - 학습 데이터의 노이즈나 비정상적인 패턴까지 학습하는 경우 발생.
- **과소적합(Underfitting)**:
  - 모델이 학습 데이터의 패턴을 충분히 학습하지 못해 일반화 성능이 낮은 상태.
  - 모델이 너무 단순하거나 학습이 충분히 이루어지지 않은 경우 발생.

### 최적화 알고리즘의 중요성

```{image} figs/image-3-4-2.jpeg
:width: 90%
:align: center
```

- **일반화 능력 향상**:
  - 최적화 알고리즘은 모델이 학습 데이터뿐만 아니라 새로운 데이터에도 잘 작동하도록 도와줍니다.
  - 모델의 일반화 능력을 향상시켜 실제 세계의 다양한 데이터에 적용 가능하게 합니다.
- **적절한 모델 복잡도**:
  - 최적화를 통해 모델의 복잡도를 조절하고, 과대적합과 과소적합 사이의 균형을 맞춥니다.

### 과대적합과 과소적합 방지 전략

```{image} figs/image-3-4-3.jpeg
:width: 90%
:align: center
```

- **데이터 증강(Data Augmentation)**:
  - 기존 데이터에 변형을 가해 데이터셋의 다양성을 증가시키는 방법.
  - 과대적합을 방지하고 모델의 일반화 능력을 향상시킵니다.
- **교차 검증(Cross-Validation)**:
  - 학습 데이터를 여러 부분으로 나누고, 이들을 교차하여 검증하는 방법.
  - 모델의 성능을 보다 객관적으로 평가할 수 있습니다.
- **정규화(Regularization)**:
  - 모델의 가중치에 제약을 두어 복잡도를 감소시키는 기술.
  - L1, L2 정규화 등이 있으며, 과대적합을 방지하는 데 효과적입니다.

## 좋은 머신러닝 모델의 조건

### 데이터의 양과 질의 중요성

```{image} figs/image-3-5-1.jpeg
:width: 90%
:align: center
```

- **데이터의 중요성**:
  - 머신러닝 모델의 성능은 사용하는 데이터의 양과 질에 크게 의존합니다.
  - 충분하고 다양한 데이터는 모델이 더 많은 패턴과 상황을 학습하게 합니다.
- **고품질 데이터의 특성**:
  - 정확하고, 완전하며, 관련성이 높은 데이터.
  - 노이즈가 적고, 편향되지 않은 데이터 셋.

### 모델 복잡도 조절

```{image} figs/image-3-5-2.jpeg
:width: 90%
:align: center
```

- **모델 복잡도의 중요성**:
  - 모델이 너무 복잡하면 과대적합의 위험이 있고, 너무 단순하면 과소적합이 발생할 수 있습니다.
- **PCA (주성분 분석)**:
  - 고차원 데이터의 차원을 축소하여 모델의 복잡도를 줄이는 기법.
  - 중요한 정보를 유지하면서 데이터의 특성 수를 감소시킵니다.

### 일반화, 정규화, 가중치 규제

```{image} figs/image-3-5-3.jpeg
:width: 90%
:align: center
```

- **일반화(Generalization)**:
  - 모델이 새로운 데이터에 대해 잘 예측하는 능력.
  - 학습 데이터뿐만 아니라 테스트 데이터에서도 좋은 성능을 나타냄을 의미합니다.
- **정규화(Regularization)**:
  - L1, L2 정규화와 같은 기법을 사용하여 모델의 과대적합을 방지합니다.
  - 모델의 가중치에 제약을 추가하여 복잡도를 줄입니다.
- **가중치 규제(Weight Regularization)**:
  - 모델의 가중치가 너무 커지지 않도록 제한하여 과대적합을 방지합니다.